from prompts.ats_prompt import build_ats_prompt
def analyze_resume(llm, resume_text, job_description):
    """
    Analyzes the resume against the job description using the provided LLM.

    Args:
        llm: The language model to use for analysis.
        resume_text (str): The text extracted from the resume.
        job_description (str): The job description text.

    Returns:
        str: The analysis result from the LLM.
    """
    prompt = build_ats_prompt(resume_text, job_description)
    response = llm.invoke(prompt)
    return response.content