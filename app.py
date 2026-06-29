import streamlit as st

from langchain_ollama import ChatOllama

from utils.file_reader import extract_text

from modules.analyzer import analyze_resume

llm = ChatOllama(model="llama3.2")

st.set_page_config(
    page_title="NextRole AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 NextRole AI")

st.caption("Your AI-powered career assistant.")

st.divider()

st.caption("Powered by Llama 3.2 • LangChain • Ollama")

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader(
        "Upload your Resume",
        type=["pdf", "docx"]
    )
    if uploaded_file is not None:
        st.success("✅ Resume uploaded successfully")
resume_text = ""
if uploaded_file:
    resume_text = extract_text(uploaded_file)

with col2:
    job_description = st.text_area(
        "Paste Job Description",
        height=250
    )
    if job_description.strip():
        st.success("✅ Job description added")

left, center, right = st.columns([1, 2, 1])

with center:
    analyze = st.button("🔍 Analyze Resume", use_container_width=True)

if analyze:

    if uploaded_file is None:
        st.warning("Please upload your resume first.")

    elif not job_description.strip():
        st.warning("Please paste the job description.")

    else:

        with st.spinner("Analyzing Resume..."):
            analysis_result = analyze_resume(llm, resume_text, job_description)

        st.divider()
        st.subheader("📊 Analysis Result")
        st.markdown(analysis_result)

if uploaded_file:
    with st.expander("View Extracted Resume"):
        st.text_area(
            "Resume",
            resume_text,
            height=300
            )