import streamlit as st
from modules.profile_manager import update_profile

# =========================================================
# Education Form
# =========================================================
def education_form(profile):

    st.subheader("🎓 Education Details")

    existing_education = profile.get("education", [])

    if existing_education and st.session_state.education_entries < len(existing_education):
        st.session_state.education_entries = len(existing_education)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("➕ Add Education"):
            st.session_state.education_entries += 1

    with col2:
        if st.button("➖ Remove Last Education"):
            if st.session_state.education_entries > 1:
                st.session_state.education_entries -= 1

    with st.form("education_form"):

        education_data = []

        for i in range(st.session_state.education_entries):

            if i < len(existing_education):
                current = existing_education[i]
            else:
                current = {}

            st.markdown(f"### Education {i + 1}")

            education_levels = [
                "Select Education Level",
                "SSC",
                "Intermediate",
                "Diploma",
                "Bachelor's",
                "Master's",
                "PhD"
            ]

            level = st.selectbox(
                "Education Level",
                education_levels,
                index=education_levels.index(
                    current.get("level", "Select Education Level")
                )
                if current.get("level", "Select Education Level") in education_levels
                else 0,
                key=f"education_level_{i}"
            )

            institution = st.text_input(
                "Institution",
                value=current.get("institution", ""),
                key=f"education_institution_{i}"
            )

            board_university = st.text_input(
                "Board / University",
                value=current.get("board_university", ""),
                key=f"education_board_university_{i}"
            )

            if level == "SSC":
                specialization = ""
            else:
                specialization = st.text_input(
                    "Specialization",
                    value=current.get("specialization", ""),
                    placeholder="e.g., MPC, Computer Science, Data Science/not applicable for SSC",
                    key=f"education_specialization_{i}"
                )

            score = st.text_input(
                "Score",
                value=current.get("score", ""),
                key=f"education_score_{i}"
            )

            score_types = ["Percentage", "CGPA"]

            score_type = st.selectbox(
                "Score Type",
                score_types,
                index=score_types.index(
                    current.get("score_type", "Percentage")
                )
                if current.get("score_type", "Percentage") in score_types
                else 0,
                key=f"education_score_type_{i}"
            )

            start_year = st.text_input(
                "Start Year",
                value=current.get("start_year", ""),
                key=f"education_start_year_{i}"
            )

            end_year = st.text_input(
                "End Year",
                value=current.get("end_year", ""),
                key=f"education_end_year_{i}"
            )

            education_data.append(
                {
                    "level": level,
                    "institution": institution,
                    "board_university": board_university,
                    "specialization": specialization,
                    "score": score,
                    "score_type": score_type,
                    "start_year": start_year,
                    "end_year": end_year
                }
            )

            st.divider()

        save = st.form_submit_button("💾 Save Education Details")

        if save:

            for idx, entry in enumerate(education_data):

                if entry["level"] == "Select Education Level":
                    st.error(f"Please select an Education Level for Education {idx + 1}.")
                    return

                if not entry["institution"].strip():
                    st.error(f"Institution is required for Education {idx + 1}.")
                    return

                if not entry["board_university"].strip():
                    st.error(f"Board / University is required for Education {idx + 1}.")
                    return

                if entry["level"] != "SSC" and not entry["specialization"].strip():
                    st.error(f"Specialization is required for Education {idx + 1}.")
                    return

                if not entry["score"].strip():
                    st.error(f"Score is required for Education {idx + 1}.")
                    return

                if not entry["score"].replace(".", "").isdigit():
                    st.error(f"Score must be a valid number for Education {idx + 1}.")
                    return

                if not entry["start_year"].strip():
                    st.error(f"Start Year is required for Education {idx + 1}.")
                    return

                if not entry["start_year"].isdigit():
                    st.error(f"Start Year must be a valid number for Education {idx + 1}.")
                    return

                if not entry["end_year"].strip():
                    st.error(f"End Year is required for Education {idx + 1}.")
                    return

                if not entry["end_year"].isdigit():
                    st.error(f"End Year must be a valid number for Education {idx + 1}.")
                    return

                if int(entry["end_year"]) < int(entry["start_year"]):
                    st.error(f"End Year cannot be earlier than Start Year for Education {idx + 1}.")
                    return

            update_profile("education", education_data)

            st.success("✅ Education Details saved successfully!")