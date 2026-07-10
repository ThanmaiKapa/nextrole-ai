import streamlit as st
from modules.profile_manager import update_profile

# =========================================================
# Projects Form
# =========================================================
def projects_form(profile):

    st.subheader("💼 Project Details")

    existing_projects = profile.get("projects", [])

    if (
        existing_projects
        and st.session_state.project_entries < len(existing_projects)
    ):
        st.session_state.project_entries = len(existing_projects)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("➕ Add Project"):
            st.session_state.project_entries += 1

    with col2:
        if st.button("➖ Remove Last Project"):
            if st.session_state.project_entries > 1:
                st.session_state.project_entries -= 1

    with st.form("projects_form"):

        project_data = []

        project_types = [
            "Select Project Type",
            "Professional",
            "Academic",
            "Personal"
        ]

        for i in range(st.session_state.project_entries):

            if i < len(existing_projects):
                current = existing_projects[i]
            else:
                current = {}

            st.markdown(f"### Project {i + 1}")

            title = st.text_input(
                "Project Title",
                value=current.get("title", ""),
                key=f"project_title_{i}"
            )

            project_type = st.selectbox(
                "Project Type",
                project_types,
                index=project_types.index(
                    current.get("project_type", "Select Project Type")
                )
                if current.get("project_type", "Select Project Type") in project_types
                else 0,
                key=f"project_type_{i}"
            )

            technologies = st.text_input(
                "Technologies Used (comma-separated)",
                value=", ".join(current.get("technologies", [])),
                placeholder="Python, Flask, SQL",
                key=f"project_technologies_{i}"
            )

            description = st.text_area(
                "Description (One point per line)",
                value="\n".join(current.get("description", [])),
                key=f"project_description_{i}"
            )

            github = st.text_input(
                "GitHub Repository (Optional)",
                value=current.get("github", ""),
                placeholder="https://github.com/username/repository",
                key=f"project_github_{i}"
            )

            project_data.append(
                {
                    "title": title,
                    "project_type": project_type,
                    "technologies": [
                        tech.strip()
                        for tech in technologies.split(",")
                        if tech.strip()
                    ],
                    "description": [
                        line.strip()
                        for line in description.split("\n")
                        if line.strip()
                    ],
                    "github": github.strip()
                }
            )

            st.divider()

        save = st.form_submit_button("💾 Save Project Details")

        if save:

            for idx, entry in enumerate(project_data):

                if not entry["title"].strip():
                    st.error(f"Project Title is required for Project {idx + 1}.")
                    return

                if entry["project_type"] == "Select Project Type":
                    st.error(f"Please select a Project Type for Project {idx + 1}.")
                    return

                if not entry["technologies"]:
                    st.error(f"Please enter at least one technology for Project {idx + 1}.")
                    return

                if not entry["description"]:
                    st.error(f"Description is required for Project {idx + 1}.")
                    return

            update_profile("projects", project_data)

            st.success("✅ Project Details saved successfully!")