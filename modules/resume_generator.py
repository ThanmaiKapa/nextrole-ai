import json

from prompts.resume_generator_prompts import (
    build_summary_prompt,
    build_experience_prompt,
    build_project_prompt
)

from modules.similarity_manager import similarity_search


# ==========================================================
# Parse Skills
# ==========================================================

def parse_skills(skill_text):

    skills = {}

    lines = skill_text.splitlines()

    for line in lines:

        line = line.strip()

        if not line or line.lower() == "skills":
            continue

        if ":" not in line:
            continue

        category, values = line.split(":", 1)

        skills[category.strip()] = [
            value.strip()
            for value in values.split(",")
            if value.strip()
        ]

    return skills


# ==========================================================
# Invoke LLM and Parse JSON
# ==========================================================

def invoke_json(llm, prompt):

    response = llm.invoke(prompt)

    if not response.content.strip():
        raise ValueError("The LLM returned an empty response.")

    content = (
        response.content
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        return json.loads(content)

    except json.JSONDecodeError:

        print("=" * 80)
        print("INVALID LLM RESPONSE")
        print(content)
        print("=" * 80)

        raise ValueError("The LLM returned invalid JSON.")


# ==========================================================
# Resume Generator
# ==========================================================

def generate_resume(llm, master_profile, job_description):

    max_projects = 4
    min_professional_projects = 2

    # ======================================================
    # Retrieved Context
    # ======================================================

    retrieved_context = {

        "personal_information":
            master_profile.get("personal_information", {}),

        "education":
            master_profile.get("education", []),

        "experience":
            master_profile.get("experience", []),

        "certifications":
            master_profile.get("certifications", []),

        "skills": {},

        "professional_projects": [],

        "academic_projects": [],

        "personal_projects": []
    }

    # ======================================================
    # Retrieve Skills
    # ======================================================

    skill_matches = similarity_search(
        job_description,
        top_k=3,
        sections=["Skills"]
    )

    skills = {}

    if skill_matches:

        skills = parse_skills(
            skill_matches[0]["text"]
        )

    # ======================================================
    # Retrieve Projects
    # ======================================================

    professional_matches = similarity_search(
        job_description,
        top_k=10,
        sections=["Project"],
        project_type="Professional"
    )

    project_matches = similarity_search(
        job_description,
        top_k=10,
        sections=["Project"]
    )

    selected_projects = []
    selected_titles = set()

    # ======================================================
    # Guarantee Professional Projects
    # ======================================================

    for project in professional_matches:

        if len(selected_projects) >= min_professional_projects:
            break

        if project["data"] is None:
            continue

        title = project["data"]["title"]

        selected_projects.append(project)

        selected_titles.add(title)

    # ======================================================
    # Fill Remaining Project Slots
    # ======================================================

    for project in project_matches:

        if len(selected_projects) >= max_projects:
            break

        if project["data"] is None:
            continue

        title = project["data"]["title"]

        if title in selected_titles:
            continue

        selected_projects.append(project)

        selected_titles.add(title)

    # ======================================================
    # Separate Projects
    # ======================================================

    for project in selected_projects:

        project_data = project["data"]

        if project_data is None:
            continue

        project_type = project_data.get("project_type")

        if project_type == "Professional":

            retrieved_context["professional_projects"].append(
                project_data
            )

        elif project_type == "Academic":

            retrieved_context["academic_projects"].append(
                project_data
            )

        elif project_type == "Personal":

            retrieved_context["personal_projects"].append(
                project_data
            )

    retrieved_context["skills"] = skills

    # ======================================================
    # Generate Professional Summary
    # ======================================================

    all_projects = (
        retrieved_context["professional_projects"]
        + retrieved_context["academic_projects"]
        + retrieved_context["personal_projects"]
    )

    summary_prompt = build_summary_prompt(
        job_description=job_description,
        personal_information=retrieved_context["personal_information"],
        skills=retrieved_context["skills"],
        experience=retrieved_context["experience"],
        projects=all_projects
    )

    summary_response = invoke_json(
        llm,
        summary_prompt
    )

    professional_summary = summary_response.get(
        "professional_summary",
        retrieved_context["personal_information"].get(
            "summary",
            ""
        )
    )

    # ======================================================
    # Rewrite Work Experience
    # ======================================================

    rewritten_experience = []

    for experience in retrieved_context["experience"]:

        experience_prompt = build_experience_prompt(
            job_description=job_description,
            experience=experience
        )

        response = invoke_json(
            llm,
            experience_prompt
        )

        rewritten_experience.append(
            response.get(
                "description",
                experience.get("description", [])
            )
        )

    # ======================================================
    # Rewrite Professional Projects
    # ======================================================

    rewritten_professional_projects = []

    for project in retrieved_context["professional_projects"]:

        project_prompt = build_project_prompt(
            job_description=job_description,
            project=project
        )

        response = invoke_json(
            llm,
            project_prompt
        )

        rewritten_professional_projects.append(
            response.get(
                "description",
                project.get("description", [])
            )
        )

    # ======================================================
    # Rewrite Academic Projects
    # ======================================================

    rewritten_academic_projects = []

    for project in retrieved_context["academic_projects"]:

        project_prompt = build_project_prompt(
            job_description=job_description,
            project=project
        )

        response = invoke_json(
            llm,
            project_prompt
        )

        rewritten_academic_projects.append(
            response.get(
                "description",
                project.get("description", [])
            )
        )

    # ======================================================
    # Rewrite Personal Projects
    # ======================================================

    rewritten_personal_projects = []

    for project in retrieved_context["personal_projects"]:

        project_prompt = build_project_prompt(
            job_description=job_description,
            project=project
        )

        response = invoke_json(
            llm,
            project_prompt
        )

        rewritten_personal_projects.append(
            response.get(
                "description",
                project.get("description", [])
            )
        )

    # ======================================================
    # Build Final Resume
    # ======================================================

    resume = {
        "personal_information": retrieved_context["personal_information"],
        "professional_summary": professional_summary,
        "skills": retrieved_context["skills"],
        "work_history": [],
        "professional_projects": [],
        "academic_projects": [],
        "personal_projects": [],
        "education": retrieved_context["education"],
        "certifications": retrieved_context["certifications"]
    }

    # ======================================================
    # Merge Work History
    # ======================================================

    for i, experience in enumerate(retrieved_context["experience"]):

        work_item = experience.copy()

        if i < len(rewritten_experience):
            work_item["description"] = rewritten_experience[i]

        resume["work_history"].append(work_item)

    # ======================================================
    # Merge Professional Projects
    # ======================================================

    for i, project in enumerate(retrieved_context["professional_projects"]):

        project_item = project.copy()

        if i < len(rewritten_professional_projects):
            project_item["description"] = rewritten_professional_projects[i]

        resume["professional_projects"].append(project_item)

    # ======================================================
    # Merge Academic Projects
    # ======================================================

    for i, project in enumerate(retrieved_context["academic_projects"]):

        project_item = project.copy()

        if i < len(rewritten_academic_projects):
            project_item["description"] = rewritten_academic_projects[i]

        resume["academic_projects"].append(project_item)

    # ======================================================
    # Merge Personal Projects
    # ======================================================

    for i, project in enumerate(retrieved_context["personal_projects"]):

        project_item = project.copy()

        if i < len(rewritten_personal_projects):
            project_item["description"] = rewritten_personal_projects[i]

        resume["personal_projects"].append(project_item)

    # ======================================================
    # Debug
    # ======================================================

    print("=" * 80)
    print("FINAL GENERATED RESUME")
    print(json.dumps(resume, indent=2, ensure_ascii=False))
    print("=" * 80)

    return resume