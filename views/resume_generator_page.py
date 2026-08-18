import streamlit as st

from modules.resume_generator import generate_resume
from modules.master_profile import master_profile
from modules.word_generator import generate_word_document

import traceback


def resume_generator_page(llm):
    """
    Streamlit page for generating an ATS-friendly resume
    based on a Job Description.
    """

    st.title("📄 Resume Generator")

    st.write(
        "Paste a Job Description below and generate an ATS-optimized resume "
        "using your Master Profile."
    )

    job_description = st.text_area(
        "Job Description",
        height=300,
        placeholder="Paste the complete Job Description here..."
    )

   # ==================================================
    # Initialize Session State
    # ==================================================

    if "generated_resume" not in st.session_state:
        st.session_state.generated_resume = None


    # ==================================================
    # Generate Resume
    # ==================================================

    if st.button("Generate Resume", use_container_width=True):

        if not job_description.strip():
            st.warning("Please enter a Job Description.")
            return

        with st.spinner("Generating Resume..."):

            try:
                resume = generate_resume(
                    llm,
                    master_profile,
                    job_description
                )

                # Store generated resume so it survives Streamlit reruns
                st.session_state.generated_resume = resume

            except Exception as e:
                traceback.print_exc()
                st.exception(e)
                return


    # ==================================================
    # Display Generated Resume / Download
    # ==================================================

    resume = st.session_state.generated_resume

    if resume:

        st.success("Resume generated successfully!")

        word_file = generate_word_document(resume)

        st.download_button(
            label="📥 Download Resume as Word Document",
            data=word_file,
            file_name="ATS_Resume.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True
        )

        st.divider()

        # ==================================================
        # Professional Summary
        # ==================================================

        st.header("Professional Summary")

        st.write(resume.get("professional_summary", ""))

        st.divider()

        # ==================================================
        # Skills
        # ==================================================

        st.header("Skills")

        skills = resume.get("skills", {})

        for category, skill_list in skills.items():

            st.subheader(category)

            if skill_list:
                for skill in skill_list:
                    st.markdown(f"- {skill}")
            else:
                st.write("No skills available.")

        st.divider()

        # ==================================================
        # Work History
        # ==================================================

        st.header("Work History")

        for work in resume.get("work_history", []):

            st.subheader(
                f"{work.get('role', '')} | {work.get('company', '')}"
            )

            if "duration" in work:
                st.caption(work["duration"])
            else:
                end_date = (
                    "Present"
                    if work.get("currently_working")
                    else work.get("end_date", "")
                )

                st.caption(
                    f"{work.get('start_date', '')} - {end_date}"
                )

            description = work.get("description", [])

            if isinstance(description, str):
                description = [description]

            for item in description:
                st.markdown(f"- {item}")

        st.divider()

        # ==================================================
        # Professional Projects
        # ==================================================

        st.header("Professional Projects")

        professional_projects = resume.get("professional_projects", [])

        if professional_projects:

            for project in professional_projects:

                st.subheader(project.get("title", ""))

                technologies = project.get("technologies", [])

                if technologies:
                    st.write(
                        "**Technologies:** "
                        + ", ".join(technologies)
                    )

                description = project.get("description", [])

                if isinstance(description, str):
                    description = [description]

                for bullet in description:
                    st.markdown(f"- {bullet}")

                if project.get("github"):
                    st.markdown(
                        f"**GitHub:** {project['github']}"
                    )

        else:
            st.write("No professional projects.")

        st.divider()

        # ==================================================
        # Academic Projects
        # ==================================================

        st.header("Academic Projects")

        academic_projects = resume.get("academic_projects", [])

        if academic_projects:

            for project in academic_projects:

                st.subheader(project.get("title", ""))

                technologies = project.get("technologies", [])

                if technologies:
                    st.write(
                        "**Technologies:** "
                        + ", ".join(technologies)
                    )

                description = project.get("description", [])

                if isinstance(description, str):
                    description = [description]

                for bullet in description:
                    st.markdown(f"- {bullet}")

                if project.get("github"):
                    st.markdown(
                        f"**GitHub:** {project['github']}"
                    )

        else:
            st.write("No academic projects.")

        st.divider()

        # ==================================================
        # Personal Projects
        # ==================================================

        st.header("Personal Projects")

        personal_projects = resume.get("personal_projects", [])

        if personal_projects:

            for project in personal_projects:

                st.subheader(project.get("title", ""))

                technologies = project.get("technologies", [])

                if technologies:
                    st.write(
                        "**Technologies:** "
                        + ", ".join(technologies)
                    )

                description = project.get("description", [])

                if isinstance(description, str):
                    description = [description]

                for bullet in description:
                    st.markdown(f"- {bullet}")

                if project.get("github"):
                    st.markdown(
                        f"**GitHub:** {project['github']}"
                    )

        else:
            st.write("No personal projects.")

        st.divider()

        # ==================================================
        # Education
        # ==================================================

        st.header("Education")

        education = resume.get("education", [])

        if education:

            for edu in education:

                st.subheader(edu.get("level", ""))

                if edu.get("institution"):
                    st.write(edu["institution"])

                if edu.get("specialization"):
                    st.write(
                        f"**Specialization:** {edu['specialization']}"
                    )

                if edu.get("board_university"):
                    st.write(
                        f"**University/Board:** {edu['board_university']}"
                    )

                if edu.get("start_year") and edu.get("end_year"):
                    st.caption(
                        f"{edu['start_year']} - {edu['end_year']}"
                    )

                if edu.get("score"):
                    score = edu["score"]

                    if edu.get("score_type"):
                        score += f" {edu['score_type']}"

                    st.write(f"**Score:** {score}")

        else:
            st.write("No education details.")

        st.divider()

        # ==================================================
        # Certifications
        # ==================================================

        st.header("Certifications")

        certifications = resume.get("certifications", [])

        if certifications:

            for cert in certifications:

                st.subheader(cert.get("name", ""))

                if cert.get("issuer"):
                    st.write(f"**Issuer:** {cert['issuer']}")

                if cert.get("issue_date"):
                    st.write(
                        f"**Issued:** {cert['issue_date']}"
                    )

                if cert.get("expiration_date"):
                    st.write(
                        f"**Expires:** {cert['expiration_date']}"
                    )

                if cert.get("credential_url"):
                    st.markdown(
                        f"**Credential:** {cert['credential_url']}"
                    )

        else:
            st.write("No certifications.")

        st.divider()

        # ==================================================
        # Raw JSON (Debug)
        # ==================================================

        with st.expander("View Raw JSON"):
            st.json(resume)