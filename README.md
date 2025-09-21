AI Resume Screening

An AI-powered resume screening system that analyzes resumes against a given job description and identifies the best-matching candidates. This project helps recruiters save time by automating the resume shortlisting process.

🔹 Features

Upload resumes (PDF/DOCX).

Extract and analyze candidate skills, education, and experience.

Compare resumes with a given Job Description (JD).

Rank candidates based on relevance score.

Easy-to-use interface built with Python (Flask/Streamlit).

🔹 Tech Stack

Python

NLP (spaCy / NLTK / Transformers)

Flask / Streamlit (for UI)

scikit-learn / cosine similarity (for matching resumes with JD)

🔹 Installation & Usage

Clone the repository:

git clone https://github.com/your-username/AI-Resume-Screening.git
cd AI-Resume-Screening


Create & activate a virtual environment:

python -m venv venv
venv\Scripts\activate   # for Windows
source venv/bin/activate  # for Mac/Linux


Install dependencies:

pip install -r requirements.txt


Run the application:

python app.py


Open your browser and go to:

http://127.0.0.1:5000/

🔹 Example Workflow

Paste a Job Description.

Upload multiple resumes.

System generates matching scores.

View a ranked list of candidates.

🔹 Future Improvements

Support for more resume formats (DOCX, TXT).

Advanced semantic matching using transformer models (BERT, RoBERTa).

Cloud deployment (Heroku, AWS, or Render).

🔹 Author

