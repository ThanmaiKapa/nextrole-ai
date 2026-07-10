import streamlit as st

from modules.profile_manager import update_profile

# =========================================================
# Personal Information Form
# =========================================================
def personal_information_form(profile):

    personal = profile.get("personal_information", {})

    with st.form("personal_information_form"):

        st.subheader("👤 Personal Information")

        full_name = st.text_input(
            "Full Name",
            value=personal.get("full_name", ""),
            key="personal_full_name"
        )

        email = st.text_input(
            "Email",
            value=personal.get("email", ""),
            key="personal_email"
        )

        phone = st.text_input(
            "Phone",
            value=personal.get("phone", ""),
            key="personal_phone"
        )

        location = st.text_input(
            "Location",
            value=personal.get("location", ""),
            key="personal_location"
        )

        linkedin = st.text_input(
            "LinkedIn",
            value=personal.get("linkedin", ""),
            key="personal_linkedin"
        )

        github = st.text_input(
            "GitHub",
            value=personal.get("github", ""),
            key="personal_github"
        )

        portfolio = st.text_input(
            "Portfolio (Optional)",
            value=personal.get("portfolio", ""),
            key="personal_portfolio"
        )

        summary = st.text_area(
            "Professional Summary",
            value=personal.get("summary", ""),
            key="personal_summary"
        )

        st.divider()

        save = st.form_submit_button("💾 Save Personal Information")

        if save:

            if not full_name.strip():
                st.error("Full Name is required.")

            elif not email.strip():
                st.error("Email is required.")

            elif "@" not in email or "." not in email:
                st.error("Please enter a valid email address.")

            elif not phone.strip():
                st.error("Mobile number is required.")

            elif not phone.isdigit():
                st.error("Mobile Number should contain only digits.")

            elif len(phone) != 10:
                st.error("Mobile Number must be 10 digits.")

            else:

                personal_information = {
                    "full_name": full_name,
                    "email": email,
                    "phone": phone,
                    "location": location,
                    "linkedin": linkedin,
                    "github": github,
                    "portfolio": portfolio,
                    "summary": summary
                }

                update_profile(
                    "personal_information",
                    personal_information
                )

                st.success("✅ Personal Information saved successfully!")