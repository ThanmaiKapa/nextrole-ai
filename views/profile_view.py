import streamlit as st

# =========================================================
# Profile View
# =========================================================
def profile_view(profile):

    st.title("👤 Master Profile")

    # =========================================================
    # Personal Information
    # =========================================================
    st.subheader("👤 Personal Information")

    personal = profile.get("personal_information", {})

    st.write(f"**Full Name:** {personal.get('full_name', '')}")
    st.write(f"**Email:** {personal.get('email', '')}")
    st.write(f"**Phone:** {personal.get('phone', '')}")
    st.write(f"**Location:** {personal.get('location', '')}")
    st.write(f"**LinkedIn:** {personal.get('linkedin', '')}")
    st.write(f"**GitHub:** {personal.get('github', '')}")
    st.write(f"**Portfolio:** {personal.get('portfolio', '')}")
    st.write(f"**Professional Summary:** {personal.get('summary', '')}")

    st.divider()

    # =========================================================
    # Education
    # =========================================================
    st.subheader("🎓 Education")

    education_list = profile.get("education", [])

    if education_list:

        for index, edu in enumerate(education_list, start=1):

            with st.expander(f"Education {index}"):

                st.write(f"**Level:** {edu.get('level', '')}")
                st.write(f"**Institution:** {edu.get('institution', '')}")
                st.write(f"**Board / University:** {edu.get('board_university', '')}")
                st.write(f"**Specialization:** {edu.get('specialization', '')}")
                st.write(f"**Score:** {edu.get('score', '')} ({edu.get('score_type', '')})")
                st.write(
                    f"**Duration:** {edu.get('start_year', '')} - {edu.get('end_year', '')}"
                )

    else:
        st.info("No education details available.")

    st.divider()

    # =========================================================
    # Experience
    # =========================================================
    st.subheader("💼 Experience")

    experience_list = profile.get("experience", [])

    if experience_list:

        for index, exp in enumerate(experience_list, start=1):

            with st.expander(f"Experience {index}"):

                st.write(f"**Company:** {exp.get('company', '')}")
                st.write(f"**Role:** {exp.get('role', '')}")
                st.write(f"**Location:** {exp.get('location', '')}")
                st.write(f"**Employment Type:** {exp.get('employment_type', '')}")
                st.write(f"**Start Date:** {exp.get('start_date', '')}")

                if exp.get("currently_working"):
                    st.write("**End Date:** Present")
                else:
                    st.write(f"**End Date:** {exp.get('end_date', '')}")

                st.write("**Description:**")

                for point in exp.get("description", []):
                    st.write(f"• {point}")

    else:
        st.info("No experience details available.")

    st.divider()

    # =========================================================
    # Skills
    # =========================================================
    st.subheader("🛠️ Skills")

    skills = profile.get("skills", {})

    st.write(f"**Programming Languages:** {', '.join(skills.get('programming_languages', []))}")
    st.write(f"**Frameworks:** {', '.join(skills.get('frameworks', []))}")
    st.write(f"**Databases:** {', '.join(skills.get('databases', []))}")
    st.write(f"**Cloud Platforms:** {', '.join(skills.get('cloud', []))}")
    st.write(f"**Tools:** {', '.join(skills.get('tools', []))}")
    st.write(f"**Soft Skills:** {', '.join(skills.get('soft_skills', []))}")

    st.divider()

    # =========================================================
    # Projects
    # =========================================================
    st.subheader("🚀 Projects")

    projects_list = profile.get("projects", [])

    if projects_list:

        for index, project in enumerate(projects_list, start=1):

            with st.expander(f"Project {index}"):

                st.write(f"**Title:** {project.get('title', '')}")
                st.write(f"**Project Type:** {project.get('project_type', '')}")

                st.write(
                    f"**Technologies:** {', '.join(project.get('technologies', []))}"
                )

                st.write("**Description:**")

                for point in project.get("description", []):
                    st.write(f"• {point}")

                if project.get("github"):
                    st.write(f"**GitHub:** {project.get('github')}")

    else:
        st.info("No project details available.")

    st.divider()

    # =========================================================
    # Certifications
    # =========================================================
    st.subheader("📜 Certifications")

    certifications_list = profile.get("certifications", [])

    if certifications_list:

        for index, cert in enumerate(certifications_list, start=1):

            with st.expander(f"Certification {index}"):

                st.write(f"**Name:** {cert.get('name', '')}")
                st.write(f"**Issuer:** {cert.get('issuer', '')}")
                st.write(f"**Issue Date:** {cert.get('issue_date', '')}")

                if cert.get("expiration_date"):
                    st.write(
                        f"**Expiration Date:** {cert.get('expiration_date')}"
                    )
                else:
                    st.write("**Expiration Date:** Does not expire")

                if cert.get("credential_url"):
                    st.write(
                        f"**Credential URL:** {cert.get('credential_url')}"
                    )

    else:
        st.info("No certification details available.")