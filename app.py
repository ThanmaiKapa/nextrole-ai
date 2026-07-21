import streamlit as st

from langchain_ollama import ChatOllama

from views.home import show_home
from views.ats_analyzer_page import show_ats
from views.master_profile import show_master_profile

from utils.session_state import initialize_session_state

llm = ChatOllama(model="llama3.2", temperature=0)

st.set_page_config(
    page_title="NextRole AI",
    page_icon="🚀",
    layout="wide"
)

initialize_session_state()

st.sidebar.title("🚀 NextRole AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📄 ATS Analyzer",
        "👤 Master Profile"
    ]
)

if page == "🏠 Home":
    show_home()

elif page == "📄 ATS Analyzer":
    show_ats(llm)

elif page == "👤 Master Profile":
    show_master_profile()