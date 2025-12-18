# Resume Analyzer using NLP

An ATS-style resume analysis system built using Natural Language Processing (NLP).
This project focuses on extracting, normalizing, and evaluating resume skills
against a job description with explainable, section-aware scoring.

The system is designed as a foundation for a future full-stack application 
aimed at helping students analyze and improve their application documents.

---

## 🔍 What This Project Does

- Extracts skills from resumes and job descriptions using rule-based NLP
- Normalizes skill variants and abbreviations (e.g., ML → Machine Learning)
- Categorizes skills (Language, Tool, Concept)
- Detects resume sections (Skills, Projects, Experience, Education)
- Tracks *where* each skill is demonstrated
- Computes a weighted resume–job match score
- Produces explainable outputs highlighting strengths and gaps
- Handles noisy resume text (PDF-to-text artifacts, formatting issues)

This project prioritizes **interpretability and reasoning** over black-box models.

---

## 🧠 Design Philosophy

Instead of relying on heavy machine learning models, this system uses:
- Structured NLP pipelines (spaCy EntityRuler)
- Explicit normalization rules
- Evidence-based reasoning
- Transparent scoring logic
---

## 📁 Project Structure

src/
run.py # Entry point
skill_e.py # Skill extraction & normalization
matcher.py # Weighted skill matching logic
section_parser.py # Resume section detection

data/
skills.csv
skill_aliases.csv
skill_weights.csv

examples/
sample_resume.txt
job_description.txt

yaml
Copy code

---

## ▶️ How to Run

### Install dependencies

pip install -r requirements.txt
python -m spacy download en_core_web_sm
Run the analyzer
bash
Copy code
cd src
python run.py
Paste the resume text, press ENTER twice, then paste the job description.

📊 Example Output
yaml
Copy code
MATCHED SKILLS
LANGUAGE: python, sql
SKILL: machine learning
TOOL: tensorflow, scikit-learn

MISSING SKILLS
SKILL: data analysis

WEIGHTED MATCH SCORE: 85.71%

SKILL EVIDENCE BY SECTION
python: SKILLS
sql: SKILLS, EXPERIENCE
machine learning: SKILLS, PROJECTS
tensorflow: PROJECTS
scikit-learn: PROJECTS

🚀 Planned Extensions (Future Work)
This project is intentionally designed to scale into a full-stack application
to support students during university and job applications.

1️⃣ Web-Based Interface
Upload or paste resume text

Upload job descriptions

View structured analysis and feedback

Built using Streamlit or React + FastAPI

2️⃣ Student-Focused Feedback Engine
Natural-language suggestions for improvement

Highlight weak or missing sections

Suggest where to add evidence for listed skills

3️⃣ SOP (Statement of Purpose) Analyzer
Analyze SOP structure (goals, background, motivation)

Detect missing components

Provide clarity and balance feedback

4️⃣ Resume Improvement Tracking
Compare multiple resume versions

Track skill coverage improvements over time

Measure alignment with different roles or programs

5️⃣ Backend API & Database
REST API for NLP analysis

Store user analyses and feedback

Support multiple documents per user

🎯 Intended Use Case
This project is aimed at:

Students applying for internships, jobs, or graduate programs

Learners exploring applied NLP and text analysis

Developers building explainable decision-support systems

It is not intended to replace professional review but to assist users in
self-evaluating and improving their documents.

📌 Current Status
NLP backend complete and stable

Modular, testable architecture

Ready for UI and API integration

Future work documented but not yet implemented
## 👤 Author

Built with ❤️ by Nimbus

