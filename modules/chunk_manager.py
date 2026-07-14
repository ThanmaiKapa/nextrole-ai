# modules/chunk_manager.py

def create_chunks(profile):
    """
    Convert the Master Profile into meaningful text chunks.
    Each chunk represents one logical section of the profile.
    """

    chunks = []

    # ==========================================================
    # Personal Information
    # ==========================================================

    personal = profile.get("personal_information", {})

    if personal:

        personal_text = "Personal Information\n\n"

        personal_text += f"Name: {personal.get('full_name', '')}\n"
        personal_text += f"Email: {personal.get('email', '')}\n"
        personal_text += f"Phone: {personal.get('phone', '')}\n"
        personal_text += f"Location: {personal.get('location', '')}\n"

        if personal.get("linkedin"):
            personal_text += f"LinkedIn: {personal['linkedin']}\n"

        if personal.get("github"):
            personal_text += f"GitHub: {personal['github']}\n"

        if personal.get("portfolio"):
            personal_text += f"Portfolio: {personal['portfolio']}\n"

        if personal.get("summary"):
            personal_text += f"\nProfessional Summary:\n{personal['summary']}"

        chunks.append(personal_text.strip())

    # ==========================================================
    # Education
    # ==========================================================

    education_list = profile.get("education", [])

    for education in education_list:

        education_text = "Education\n\n"

        education_text += f"Level: {education.get('level', '')}\n"
        education_text += f"Institution: {education.get('institution', '')}\n"
        education_text += (
            f"Board / University: {education.get('board_university', '')}\n"
        )

        # Specialization is optional for SSC
        if education.get("specialization"):
            education_text += (
                f"Specialization: {education['specialization']}\n"
            )

        education_text += (
            f"Score: {education.get('score', '')} "
            f"{education.get('score_type', '')}\n"
        )

        education_text += (
            f"Duration: "
            f"{education.get('start_year', '')} - "
            f"{education.get('end_year', '')}"
        )

        chunks.append(education_text.strip())

    # ==========================================================
    # Experience
    # ==========================================================

    experience_list = profile.get("experience", [])

    for experience in experience_list:

        experience_text = "Experience\n\n"

        experience_text += (
            f"Company: {experience.get('company', '')}\n"
        )

        experience_text += (
            f"Role: {experience.get('role', '')}\n"
        )

        experience_text += (
            f"Location: {experience.get('location', '')}\n"
        )

        experience_text += (
            f"Employment Type: "
            f"{experience.get('employment_type', '')}\n"
        )

        experience_text += (
            f"Start Date: {experience.get('start_date', '')}\n"
        )

        if experience.get("currently_working"):
            experience_text += "End Date: Present\n"
        else:
            experience_text += (
                f"End Date: {experience.get('end_date', '')}\n"
            )

        description = experience.get("description", [])

        if description:
            experience_text += "\nResponsibilities:\n"

            for point in description:
                experience_text += f"- {point}\n"

        chunks.append(experience_text.strip())

    # ==========================================================
    # Skills
    # ==========================================================

    skills = profile.get("skills", {})

    if skills:

        skills_text = "Skills\n\n"

        if skills.get("programming_languages"):
            skills_text += (
                "Programming Languages: "
                + ", ".join(skills["programming_languages"])
                + "\n"
            )

        if skills.get("frameworks"):
            skills_text += (
                "Frameworks: "
                + ", ".join(skills["frameworks"])
                + "\n"
            )

        if skills.get("databases"):
            skills_text += (
                "Databases: "
                + ", ".join(skills["databases"])
                + "\n"
            )

        if skills.get("cloud"):
            skills_text += (
                "Cloud: "
                + ", ".join(skills["cloud"])
                + "\n"
            )

        if skills.get("tools"):
            skills_text += (
                "Tools: "
                + ", ".join(skills["tools"])
                + "\n"
            )

        if skills.get("soft_skills"):
            skills_text += (
                "Soft Skills: "
                + ", ".join(skills["soft_skills"])
                + "\n"
            )

        chunks.append(skills_text.strip())

    # ==========================================================
    # Projects
    # ==========================================================

    project_list = profile.get("projects", [])

    for project in project_list:

        project_text = "Project\n\n"

        project_text += (
            f"Title: {project.get('title', '')}\n"
        )

        project_text += (
            f"Project Type: {project.get('project_type', '')}\n"
        )

        technologies = project.get("technologies", [])

        if technologies:
            project_text += (
                "Technologies: "
                + ", ".join(technologies)
                + "\n"
            )

        description = project.get("description", [])

        if description:

            project_text += "\nDescription:\n"

            for point in description:
                project_text += f"- {point}\n"

        if project.get("github"):
            project_text += (
                f"\nGitHub: {project['github']}"
            )

        chunks.append(project_text.strip())

    # ==========================================================
    # Certifications
    # ==========================================================

    certification_list = profile.get("certifications", [])

    for certification in certification_list:

        certification_text = "Certification\n\n"

        certification_text += (
            f"Name: {certification.get('name', '')}\n"
        )

        certification_text += (
            f"Issuer: {certification.get('issuer', '')}\n"
        )

        certification_text += (
            f"Issue Date: {certification.get('issue_date', '')}\n"
        )

        if certification.get("expiration_date"):
            certification_text += (
                f"Expiration Date: "
                f"{certification['expiration_date']}\n"
            )
        else:
            certification_text += (
                "Expiration Date: Does Not Expire\n"
            )

        if certification.get("credential_url"):
            certification_text += (
                f"Credential URL: "
                f"{certification['credential_url']}\n"
            )

        chunks.append(certification_text.strip())

    return chunks