import streamlit as st

def initialize_session_state():

    defaults = {
        "create_profile": False,
        "edit_profile": False,
        "view_profile": False,
        "profile_form_open": False,   
        "education_entries": 1,
        "experience_entries": 1,
        "project_entries": 1,
        "certification_entries": 1
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value