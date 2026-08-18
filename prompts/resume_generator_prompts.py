import json

def build_summary_prompt(
    job_description,
    personal_information,
    skills,
    experience,
    projects
):

    prompt = f"""
you are a professional ats resume writer 

Rewrite the CURRENT PROFESSIONAL SUMMARY using stronger action verbs and clearer professional language. Preserve the original meaning exactly. Do not add, remove, infer, or replace any technologies, responsibilities, achievements, or business domains. Improve grammar and readability only by following the given structure below

================================================
SAMPLE SUMMARY STRUCTURE
================================================

Current profession({experience[-1]["role"]}) with years of experience(for example: 1+, 2+,..) followed by the candidate's core professional skills. Highlight key technologies, responsibilities, and technical strengths demonstrated through professional work experience(only from provided EXPERIENCE). Highlight advanced technical expertise gained through personal and professional projects such as LLMs, LangChain, RAG, ChromaDB, Vector Databases, Embeddings, Prompt Engineering, AI/ML, Microsoft Fabric, etc., ONLY if they exist in the provided SKILLS. Conclude with the candidate's strongest technical capabilities and value relevant to the target role.

=================================================
CURRENT PROFESSIONAL SUMMARY
=================================================

{personal_information.get("summary", "")}

==================================================
JOB DESCRIPTION
==================================================

{job_description}

==================================================
WORK EXPERIENCE
==================================================

{json.dumps(experience, indent=2, ensure_ascii=False)}

==================================================
SKILLS
==================================================

{json.dumps(skills, indent=2, ensure_ascii=False)}

==================================================
PROJECTS
==================================================

{json.dumps(projects, indent=2, ensure_ascii=False)}

============
RULES
============
Provided SKILLS, EXPERIENCE, PROJECTS are the only source of truth do not invent or add any thing that is not present in them and use JOB DESCRIPTION only to prioritize relevant experience and skills and only use provided EXPERIENCE and SKILLS 

only mention role and skills from EXPERIENCE and SKILLS provided

only follow given sample summary structure and do not add any new information or change the meaning of the summary

==================================================
OUTPUT
==================================================

Return ONLY valid JSON.

{{
    "professional_summary": ""
}}
"""

    return prompt

def build_experience_prompt(
    job_description,
    experience
):

    prompt = f"""
You are an expert ATS Resume Writer.

Your task is to rewrite ONLY the work experience description.

The provided work experience is the ONLY source of truth.

The Job Description is used ONLY to improve wording and emphasize relevant existing experience.

Never add information that is not supported by the work experience.

==================================================
JOB DESCRIPTION
==================================================

{job_description}

==================================================
WORK EXPERIENCE
==================================================

{json.dumps(experience, indent=2, ensure_ascii=False)}

==================================================
RULES
==================================================

Rewrite ONLY the description field.

Use ONLY the information provided in the work experience.

Preserve the original meaning.

Preserve all existing technologies, tools, frameworks, and business domains.

If the original description contains important technologies (for example Python, SQL, Power BI, Microsoft Fabric, Tableau, etc.), keep them whenever they accurately describe the work.

Do NOT remove important technical keywords that improve ATS matching.

Do NOT invent:

- responsibilities
- technologies
- tools
- frameworks
- achievements
- business domains
- projects
- metrics

Do NOT copy responsibilities or sentences directly from the Job Description.

Do NOT change:

- company
- role
- location
- employment type
- start date
- end date
- currently working status

Improve wording using professional language and strong action verbs.

Make the description more ATS-friendly while keeping it truthful.

Keep measurable achievements whenever they already exist.

Keep the rewritten description concise (1–2 sentences).

If the existing description is already strong and ATS-friendly, make only minor wording improvements instead of rewriting it completely.

==================================================
OUTPUT
==================================================

Return ONLY valid JSON.

{{
    "description": []
}}
"""

    return prompt

def build_project_prompt(
    job_description,
    project
):

    prompt = f"""
You are an expert ATS Resume Writer.

Your task is to rewrite ONLY the project description.

The provided project is the ONLY source of truth.

The Job Description must NEVER change the technical scope of the project.

Use the Job Description ONLY to improve wording and prioritize existing ATS keywords.

If the Job Description mentions technologies, frameworks, APIs, cloud services, responsibilities, or business domains that are NOT already present in the project, DO NOT add them.

Never add information that is not supported by the project.

==================================================
JOB DESCRIPTION
==================================================

{job_description}

==================================================
PROJECT
==================================================

{json.dumps(project, indent=2, ensure_ascii=False)}

==================================================
RULES
==================================================

Rewrite ONLY the description.

The goal is to improve readability and ATS optimization, NOT to change the technical content.

Use ONLY the information provided in the project.

Preserve the original meaning.

Preserve all existing technologies, tools, frameworks, libraries, and technical concepts.

Preserve measurable achievements, outcomes, and business impact whenever they already exist.

If the project already contains strong ATS keywords, retain them.

The rewritten description should describe exactly the same project.

Imagine that another person reads both versions.

They should conclude they are describing the SAME project using different wording.

Do not transform the project into a different project.

If the original description is already ATS-friendly, make only small wording improvements.

Do not rewrite aggressively.

Do NOT invent:

- technologies
- tools
- frameworks
- libraries
- features
- achievements
- metrics
- business impact
- responsibilities
- datasets
- APIs
- cloud platforms

Do NOT copy sentences directly from the Job Description.

Do NOT change:

- title
- technologies
- github
- project type

Improve wording using professional language and strong action verbs.

Use concise, ATS-friendly bullet points.

Keep every bullet focused on a single accomplishment or responsibility.

Do NOT remove important technical keywords that improve ATS matching.

If the existing description is already strong, make only minor wording improvements.

==================================================
OUTPUT
==================================================

Return ONLY valid JSON.

{{
    "description": []
}}
"""

    return prompt