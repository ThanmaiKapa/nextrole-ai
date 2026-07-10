import streamlit as st
from datetime import date
from modules.profile_manager import update_profile

# ========================================================
# Certifications Form
# ========================================================
def certifications_form(profile):

    st.subheader("📜 Certifications")

    existing_certifications = profile.get("certifications", [])

    if (
        existing_certifications
        and st.session_state.certification_entries < len(existing_certifications)
    ):
        st.session_state.certification_entries = len(existing_certifications)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("➕ Add Certification"):
            st.session_state.certification_entries += 1

    with col2:
        if st.button("➖ Remove Last Certification"):
            if st.session_state.certification_entries > 1:
                st.session_state.certification_entries -= 1

    with st.form("certifications_form"):

        certification_data = []

        for i in range(st.session_state.certification_entries):

            if i < len(existing_certifications):
                current = existing_certifications[i]
            else:
                current = {}

            st.markdown(f"### Certification {i + 1}")

            name = st.text_input(
                "Certification Name",
                value=current.get("name", ""),
                key=f"certification_name_{i}"
            )

            issuer = st.text_input(
                "Issuer",
                value=current.get("issuer", ""),
                key=f"certification_issuer_{i}"
            )

            issue_date = st.date_input(
                "Issue Date",
                value=date.fromisoformat(current["issue_date"])
                if current.get("issue_date")
                else date.today(),
                key=f"certification_issue_date_{i}"
            )

            no_expiration = st.checkbox(
                "This certification does not expire",
                value=current.get("expiration_date") is None,
                key=f"certification_no_expiration_{i}"
            )

            if no_expiration:
                expiration_date = None
            else:
                expiration_date = st.date_input(
                    "Expiration Date",
                    value=date.fromisoformat(current["expiration_date"])
                    if current.get("expiration_date")
                    else date.today(),
                    key=f"certification_expiration_date_{i}"
                )

            credential_url = st.text_input(
                "Credential URL (Optional)",
                value=current.get("credential_url", ""),
                placeholder="https://www.example.com/certificate",
                key=f"certification_credential_url_{i}"
            )

            certification_data.append(
                {
                    "name": name,
                    "issuer": issuer,
                    "issue_date": issue_date.isoformat(),
                    "expiration_date": None if no_expiration else expiration_date.isoformat(),
                    "credential_url": credential_url.strip()
                }
            )

            st.divider()

        save = st.form_submit_button("💾 Save Certification Details")

        if save:

            for idx, entry in enumerate(certification_data):

                if not entry["name"].strip():
                    st.error(f"Certification Name is required for Certification {idx + 1}.")
                    return

                if not entry["issuer"].strip():
                    st.error(f"Issuer is required for Certification {idx + 1}.")
                    return

                if (
                    entry["expiration_date"] is not None
                    and entry["expiration_date"] < entry["issue_date"]
                ):
                    st.error(
                        f"Expiration Date cannot be earlier than Issue Date for Certification {idx + 1}."
                    )
                    return

            update_profile("certifications", certification_data)

            st.success("✅ Certification Details saved successfully!")