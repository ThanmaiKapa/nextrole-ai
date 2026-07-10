import streamlit as st
from datetime import date
from modules.profile_manager import update_profile

# =========================================================
# Experience Form
# =========================================================
def experience_form(profile):

    st.subheader("💼 Experience Details")

    existing_experience = profile.get("experience", [])

    if (
        existing_experience
        and st.session_state.experience_entries < len(existing_experience)
    ):
        st.session_state.experience_entries = len(existing_experience)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("➕ Add Experience"):
            st.session_state.experience_entries += 1

    with col2:
        if st.button("➖ Remove Last Experience"):
            if st.session_state.experience_entries > 1:
                st.session_state.experience_entries -= 1

    with st.form("experience_form"):

        experience_data = []

        employment_types = [
            "Select Employment Type",
            "Full-time",
            "Part-time",
            "Contract",
            "Internship",
            "Freelance",
            "Self-employed"
        ]

        for i in range(st.session_state.experience_entries):

            if i < len(existing_experience):
                current = existing_experience[i]
            else:
                current = {}

            st.markdown(f"### Experience {i + 1}")

            company = st.text_input(
                "Company",
                value=current.get("company", ""),
                key=f"experience_company_{i}"
            )

            role = st.text_input(
                "Role",
                value=current.get("role", ""),
                key=f"experience_role_{i}"
            )

            location = st.text_input(
                "Location",
                value=current.get("location", ""),
                key=f"experience_location_{i}"
            )

            employment_type = st.selectbox(
                "Employment Type",
                employment_types,
                index=employment_types.index(
                    current.get("employment_type", "Select Employment Type")
                )
                if current.get("employment_type", "Select Employment Type") in employment_types
                else 0,
                key=f"experience_employment_type_{i}"
            )

            start_date = st.date_input(
                "Start Date",
                value=date.fromisoformat(current["start_date"])
                if current.get("start_date")
                else date.today(),
                key=f"experience_start_date_{i}"
            )

            currently_working = st.checkbox(
                "I currently work here",
                value=current.get("currently_working", False),
                key=f"experience_currently_working_{i}"
            )

            if currently_working:
                end_date = None
            else:
                end_date = st.date_input(
                    "End Date",
                    value=date.fromisoformat(current["end_date"])
                    if current.get("end_date")
                    else date.today(),
                    key=f"experience_end_date_{i}"
                )

            description = st.text_area(
                "Description (One point per line)",
                value="\n".join(current.get("description", [])),
                key=f"experience_description_{i}"
            )

            experience_data.append(
                {
                    "company": company,
                    "role": role,
                    "location": location,
                    "employment_type": employment_type,
                    "start_date": start_date.isoformat(),
                    "currently_working": currently_working,
                    "end_date": None if currently_working else end_date.isoformat(),
                    "description": [
                        line.strip()
                        for line in description.split("\n")
                        if line.strip()
                    ]
                }
            )

            st.divider()

        save = st.form_submit_button("💾 Save Experience Details")

        if save:

            for idx, entry in enumerate(experience_data):

                if not entry["company"].strip():
                    st.error(f"Company is required for Experience {idx + 1}.")
                    return

                if not entry["role"].strip():
                    st.error(f"Role is required for Experience {idx + 1}.")
                    return

                if not entry["location"].strip():
                    st.error(f"Location is required for Experience {idx + 1}.")
                    return

                if entry["employment_type"] == "Select Employment Type":
                    st.error(
                        f"Please select an Employment Type for Experience {idx + 1}."
                    )
                    return

                if (
                    not entry["currently_working"]
                    and entry["end_date"] < entry["start_date"]
                ):
                    st.error(
                        f"End Date cannot be earlier than Start Date for Experience {idx + 1}."
                    )
                    return

                if not entry["description"]:
                    st.error(
                        f"Description is required for Experience {idx + 1}."
                    )
                    return

            update_profile("experience", experience_data)

            st.success("✅ Experience Details saved successfully!")