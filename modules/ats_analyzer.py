import json

from prompts.ats_prompt import build_ats_prompt
from modules.similarity_manager import similarity_search
from modules.validator import build_overall_summary, validate_response
from modules.master_profile import master_profile

"""
ats_analyzer.py

Coordinates the ATS analysis workflow by reading the resume,
retrieving relevant Master Profile information, invoking the LLM,
and validating the generated response.
"""

def analyze_resume(llm, resume_text, job_description):

    matches = similarity_search(job_description, top_k=7)

    context_parts = []

    for match in matches:

        context_parts.append(
            f"{match['section']}\n"
            + "-" * 40 + "\n"
            + match["text"]
        )

    if context_parts:
        retrieved_context = "\n\n".join(context_parts)
    else:
        retrieved_context = "No relevant Master Profile information found."

    prompt = build_ats_prompt(
        resume_text,
        job_description,
        retrieved_context
    )

    response = llm.invoke(prompt)

    analysis = json.loads(response.content)

    validated = validate_response(
        analysis,
        master_profile
    )

    validated = build_overall_summary(validated)

    return validated