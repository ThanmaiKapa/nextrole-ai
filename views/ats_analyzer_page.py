import streamlit as st

from utils.file_reader import extract_text
from modules.ats_analyzer import analyze_resume

def show_ats(llm):
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
                analysis_result = analyze_resume(
                    llm,
                    resume_text,
                    job_description
                )

            st.divider()

            st.subheader("📊 ATS Analysis Report")

            # ----------------------------------------
            # ATS Scores
            # ----------------------------------------

            col1, col2 = st.columns(2)

            with col1:
                score = analysis_result["ats_compatibility"]
                st.metric(
                    "ATS Compatibility",
                    f"{score}%",
                    help="Measures how well your resume matches the job description."
                )
                st.progress(score / 100)

            with col2:
                score = analysis_result["ats_quality"]
                st.metric(
                    "ATS Quality",
                    f"{score}%",
                    help="Evaluates the overall structure and quality of your resume."
                )
                st.progress(score / 100)

            st.divider()

            # ----------------------------------------
            # Strengths
            # ----------------------------------------

            st.subheader("💪 Strengths")
            
            if analysis_result["strengths"]:
                for strength in analysis_result["strengths"]:
                    st.markdown(f"- {strength}")
            else:
                st.info("No significant strengths identified.")

            # ----------------------------------------
            # Matching Skills
            # ----------------------------------------

            st.subheader("✅ Matching Skills")

            if analysis_result["matching_skills"]:
                for skill in analysis_result["matching_skills"]:
                    st.markdown(f"- {skill}")
            else:
                st.info("No matching skills identified.")

            # ----------------------------------------
            # Additional Relevant Skills
            # ----------------------------------------

            if analysis_result["additional_master_profile_skills"]:

                st.subheader("⭐ Additional Relevant Skills")

                for skill in analysis_result["additional_master_profile_skills"]:
                    st.markdown(f"- {skill}")

            # ----------------------------------------
            # Missing Skills
            # ----------------------------------------

            st.subheader("❌ Missing Skills")

            if analysis_result["missing_skills"]:

                for skill in analysis_result["missing_skills"]:
                    st.markdown(f"- {skill}")

            else:
                st.info("No missing skills identified.")

            # ----------------------------------------
            # Weaknesses
            # ----------------------------------------

            st.subheader("⚠️ Weaknesses")

            if analysis_result["weaknesses"]:

                for weakness in analysis_result["weaknesses"]:
                    st.markdown(f"- {weakness}")

            else:
                st.info("No significant weaknesses identified.")

            # ----------------------------------------
            # Recommendations
            # ----------------------------------------

            st.subheader("💡 Recommendations")

            if analysis_result["recommendations"]:
                for rec in analysis_result["recommendations"]:

                    with st.container(border=True):

                        st.markdown(f"### {rec['problem']}")

                        st.markdown("**Why it matters**")
                        st.write(rec["why_it_matters"])

                        st.markdown("**Suggested Improvement**")
                        st.write(rec["suggested_improvement"])
            
            else:
                st.info("No additional recommendations.")

            # ----------------------------------------
            # Overall Recommendation
            # ----------------------------------------

            rating = analysis_result["overall_recommendation"]["rating"]

            st.subheader("🎯 Overall Recommendation")

            if rating == "Excellent Match":
                st.success(rating)

            elif rating == "Strong Match":
                st.success(rating)

            elif rating == "Moderate Match":
                st.warning(rating)

            else:  # Weak Match
                st.error(rating)

            st.write(analysis_result["overall_recommendation"]["summary"])