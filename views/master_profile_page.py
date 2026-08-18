import streamlit as st

from modules.profile_manager import profile_exists
from forms.personal_information_form import personal_information_form
from forms.education_form import education_form
from forms.experience_form import experience_form
from forms.skills_form import skills_form
from forms.projects_form import projects_form
from forms.certifications_form import certifications_form
from views.profile_view import profile_view

from modules.profile_manager import load_profile

def render_profile_forms(profile):

    personal_information_form(profile)
    st.divider()

    education_form(profile)
    st.divider()

    experience_form(profile)
    st.divider()

    skills_form(profile)
    st.divider()

    projects_form(profile)
    st.divider()

    certifications_form(profile)


def show_master_profile():

    profile = load_profile() or {}

    st.title("👤 Master Profile")

    if profile_exists():

        st.success("Master Profile Found")

        if not st.session_state.profile_form_open:

            col1, col2 = st.columns(2)

            with col1:
                if st.button("✏️ Edit Profile"):
                    st.session_state.profile_form_open = True
                    st.session_state.view_profile = False
                    st.rerun()

            with col2:
                if st.button("👁️ View Profile"):
                    st.session_state.view_profile = True
                    st.session_state.profile_form_open = False
                    st.rerun()

        if st.session_state.view_profile:
            profile_view(profile)

    else:

        st.warning("No Master Profile Found")

        st.write("""
Create your Master Profile once.

NextRole AI will use this information across all features.
""")

        st.markdown("""
- ✅ ATS Resume Analyzer
- ✅ Resume Generator
""")

        st.divider()

        if st.button("➕ Create Profile"):
            st.session_state.profile_form_open = True

    # -----------------------------
    # Profile Editor (Common Section)
    # -----------------------------

    if st.session_state.profile_form_open:

        st.divider()

        if st.button("❌ Close Editor"):
            st.session_state.profile_form_open = False
            st.session_state.view_profile = False
            st.rerun()

        render_profile_forms(profile)