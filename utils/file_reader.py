from pypdf import PdfReader
from docx import Document

def extract_text(uploaded_file):

    resume_text = ""

    if uploaded_file.type == "application/pdf":

        reader = PdfReader(uploaded_file)

        for page in reader.pages:
            text = page.extract_text()

            if text:
                resume_text += text + "\n"

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":

        doc = Document(uploaded_file)

        for paragraph in doc.paragraphs:

            if paragraph.text.strip():
                resume_text += paragraph.text + "\n"

    return resume_text