import streamlit as st
from modules.profile_manager import update_profile

# =========================================================
# Skills Form
# =========================================================
def skills_form(profile):

    skills = profile.get("skills", {})

    with st.form("skills_form"):

        st.subheader("🛠️ Skills")

        programming_languages = st.text_area(
            "Enter your programming languages (comma-separated)",
            value=", ".join(skills.get("programming_languages", [])),
            placeholder="e.g., Python, Java, SQL",
            key="skills_programming_languages"
        )

        frameworks = st.text_area(
            "Enter your frameworks (comma-separated)",
            value=", ".join(skills.get("frameworks", [])),
            placeholder="e.g., LangChain, Django, Flask",
            key="skills_frameworks"
        )

        databases = st.text_area(
            "Enter your databases (comma-separated)",
            value=", ".join(skills.get("databases", [])),
            placeholder="e.g., MySQL, PostgreSQL, MongoDB",
            key="skills_databases"
        )

        cloud = st.text_area(
            "Enter your cloud platforms (comma-separated)",
            value=", ".join(skills.get("cloud", [])),
            placeholder="e.g., AWS, Azure, GCP",
            key="skills_cloud"
        )

        tools = st.text_area(
            "Enter your tools (comma-separated)",
            value=", ".join(skills.get("tools", [])),
            placeholder="e.g., Git, Power BI, Tableau, VS Code",
            key="skills_tools"
        )

        soft_skills = st.text_area(
            "Enter your soft skills (comma-separated)",
            value=", ".join(skills.get("soft_skills", [])),
            placeholder="e.g., Communication, Teamwork, Problem-solving",
            key="skills_soft_skills"
        )

        st.divider()

        save = st.form_submit_button("💾 Save Skills Details")

        if save:

            if (
                not programming_languages.strip()
                and not frameworks.strip()
                and not databases.strip()
                and not cloud.strip()
                and not tools.strip()
                and not soft_skills.strip()
            ):
                st.error("Please enter at least one skill.")
                return

            skills_data = {
                "programming_languages": [
                    lang.strip()
                    for lang in programming_languages.split(",")
                    if lang.strip()
                ],
                "frameworks": [
                    fw.strip()
                    for fw in frameworks.split(",")
                    if fw.strip()
                ],
                "databases": [
                    db.strip()
                    for db in databases.split(",")
                    if db.strip()
                ],
                "cloud": [
                    cl.strip()
                    for cl in cloud.split(",")
                    if cl.strip()
                ],
                "tools": [
                    tool.strip()
                    for tool in tools.split(",")
                    if tool.strip()
                ],
                "soft_skills": [
                    skill.strip()
                    for skill in soft_skills.split(",")
                    if skill.strip()
                ]
            }

            update_profile("skills", skills_data)

            st.success("✅ Skills saved successfully!")