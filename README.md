# 🚀 NextRole AI

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![Ollama](https://img.shields.io/badge/Ollama-Llama3.2-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

An AI-powered career assistant built with Streamlit, LangChain, Ollama, and Llama 3.2. NextRole AI helps users analyze resumes against job descriptions, maintain a reusable Master Profile, and lays the foundation for AI-powered resume generation, cover letter creation, and interview preparation.

## Problem Statement

Professionals often apply for multiple job roles, but a single resume cannot effectively represent every skill, project, and experience. As a result, resumes frequently receive low ATS scores because important skills relevant to a specific job description are missing.

NextRole AI analyzes resumes against job descriptions using Retrieval-Augmented Generation (RAG). It retrieves relevant information from a reusable Master Profile, validates AI-generated responses, and provides accurate ATS-style feedback with strengths, missing skills, weaknesses, and actionable recommendations.

## Features

### 📄 ATS Resume Analyzer

- Upload resumes in PDF and DOCX formats
- Extract resume text automatically
- Paste any job description
- Analyze resumes using Llama 3.2
- Retrieval-Augmented ATS Analysis (RAG)
- Generate ATS compatibility and ATS quality scores
- Identify matching skills
- Identify additional relevant skills from the Master Profile
- Identify missing skills
- Identify weaknesses
- Generate actionable improvement recommendations
- Provide an overall candidate recommendation
- Validate AI-generated responses using a post-processing pipeline

### 👤 Master Profile

- Create and maintain a reusable professional profile
- Edit previously saved information
- View profile in a structured format
- Support multiple Education entries
- Support multiple Experience entries
- Support multiple Projects
- Support multiple Certifications
- Manage technical and professional skills
- Section-wise saving
- Input validation
- JSON-based local storage

### 🧠 Embeddings & Semantic Search

- Convert the Master Profile into meaningful text chunks
- Generate embeddings using **nomic-embed-text**
- Automatically regenerate embeddings whenever the profile is updated
- Retrieve the most relevant profile information for a given job description

### 🗄️ ChromaDB Integration

- Store profile embeddings in a persistent ChromaDB collection
- Organize embeddings using collections, documents, IDs, and metadata
- Automatically update the vector database whenever the Master Profile changes
- Perform semantic retrieval using ChromaDB nearest-neighbor search
- Eliminate manual cosine similarity computation

### 🤖 Intelligent ATS Analysis

- Retrieval-Augmented Generation (RAG)
- Response validation pipeline
- Duplicate removal
- Semantic skill validation
- Recommendation validation
- Overall recommendation generation

### ⚡ General
- Runs completely locally using Ollama
- No OpenAI API required
- Modular project architecture

## Why Local LLM?

NextRole AI runs entirely on local AI models through Ollama, using Llama 3.2 for language generation and nomic-embed-text for embedding generation.

- Run without an internet connection
- Avoid API costs
- Keep resume data on the local machine
- Experiment with LLMs without relying on external services

## Tech Stack

| Component        | Technology         |
| ---------------- | ------------------ |
| Frontend         | Streamlit          |
| Backend          | Python             |
| AI Framework     | LangChain          |
| LLM              | Llama 3.2          |
| Embedding Model  | nomic-embed-text   |
| Vector Database  | ChromaDB           |
| Local Runtime    | Ollama             |
| Document Parsing | pypdf, python-docx |
| IDE              | VS Code            |
| Data Storage     | JSON, ChromaDB     |


## Project Structure
```
NextRole_AI/
│
├── app.py
│
├── data/
│   ├── master_profile.json
│   └── chroma_db/
│
├── forms/
│   ├── personal_information_form.py
│   ├── education_form.py
│   ├── experience_form.py
│   ├── skills_form.py
│   ├── projects_form.py
│   └── certifications_form.py
│
├── modules/
│   ├── ats_analyzer.py
│   ├── chunk_manager.py
│   ├── embedding_manager.py
│   ├── profile_manager.py
│   ├── chroma_manager.py
│   ├── master_profile.py
│   ├── validator.py
│   └── similarity_manager.py
│
├── prompts/
│   └── ats_prompt.py
│
├── utils/
│   ├── file_reader.py
│   └── session_state.py
│
├── views/
│   ├── ats_analyzer_page.py
│   ├── home.py
│   ├── master_profile.py
│   └── profile_view.py
│
├── images/
│
├── requirements.txt
├── README.md
└── LICENSE
```

## Prerequisites

Before running the project, ensure you have:

- Python 3.10 or later
- Git
- Ollama installed
- Llama 3.2 downloaded
- nomic-embed-text downloaded

## Installation

1. Clone the repository

```bash
git clone https://github.com/ThanmaiKapa/nextrole-ai
```
2. Move into the project
```bash
cd nextrole-ai
```
3. Create virtual environment
```bash
python -m venv venv
```
4. Activate virtual environment

Windows
```bash
venv\Scripts\activate
```
Mac/Linux
```bash
source venv/bin/activate
```
5. Install dependencies
```bash
pip install -r requirements.txt
```
6. Install Ollama

Visit **https://ollama.com** to Install

7. Download Required Models
```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```
8. Run the application
```bash
streamlit run app.py
```
## Usage

### ATS Resume Analyzer

1. Upload your resume (PDF or DOCX).
2. Paste the target job description.
3. Click **Analyze Resume**.
4. Review the ATS score and recommendations.

### Master Profile

1. Open **Master Profile**.
2. Create your professional profile.
3. Add education, experience, skills, projects, and certifications.
4. Save each section independently.
5. View or edit your profile at any time.

## Application Screenshots

### Home Page
![Home Page](images/home_page.png)

### Resume and JD upload
![Resume and JD upload](images/upload.png)

### Resume analysis
![Resume analysis](images/resume_analysis.png)

### Master Profile

#### Create Profile
![Create Profile](images/create_profile.png)

#### Edit Profile
![Edit Profile](images/edit_profile.png)

#### View Profile
![View Profile](images/view_profile.png)

## Workflow

```
                     Start
                       │
                       ▼
                Open NextRole AI
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
   ATS Resume Analyzer       Master Profile
          │                         │
          ▼                         ▼
 Upload Resume              Create/Edit Profile
          │                         │
          ▼                         ▼
 Extract Resume Text      Save Professional Details
          │                         │
          ▼                         ▼
Paste Job Description      Store Master Profile (JSON)
          │                         │
          ▼                         ▼
 Retrieve Relevant         Generate Profile Chunks
 Master Profile Context            │
          │                        ▼
          ▼                Generate Embeddings
     Build ATS Prompt              │
          │                        ▼
          ▼                Update ChromaDB
      LangChain
          │
          ▼
       Ollama
          │
          ▼
      Llama 3.2
          │
          ▼
 Generate Structured
     ATS Analysis
          │
          ▼
 Validate AI Response
          │
          ▼
 Generate Overall
 Recommendation
          │
          ▼
 Display ATS Report
```

## Roadmap

- [x] Version 1.0 - ATS Resume Analyzer
- [x] Version 2.0 - Master Profile
- [x] Version 3.0 - Embeddings
- [x] Version 4.0 - ChromaDB
- [x] Version 5.0 - Retrieval-Augmented ATS Analysis
- [ ] Version 6.0 - AI Resume Generator
- [ ] Version 7.0 - Cover Letter Generator

## Project Status

🚧 Active Development

Current Version: **v5.0**

The project currently includes an ATS Resume Analyzer, Master Profile management, automatic embedding generation, ChromaDB-powered semantic retrieval, Retrieval-Augmented Generation (RAG), and response validation for more accurate ATS analysis.

## Future Enhancements

- AI Resume Generator
- Cover Letter Generator

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

**Thanmai Kapa**
- GitHub: https://github.com/ThanmaiKapa
- LinkedIn: https://www.linkedin.com/in/thanmai-kapa/