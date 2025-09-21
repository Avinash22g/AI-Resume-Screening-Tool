import docx2txt
from pdfminer.high_level import extract_text
from sentence_transformers import SentenceTransformer, util

# Load AI model
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_resume_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_text(file_path)
    elif file_path.endswith(".docx"):
        return docx2txt.process(file_path)
    else:
        return ""

def calculate_similarity(resume_text, job_desc):
    resume_emb = model.encode(resume_text, convert_to_tensor=True)
    jd_emb = model.encode(job_desc, convert_to_tensor=True)
    score = util.pytorch_cos_sim(resume_emb, jd_emb).item()
    return round(score * 100, 2)
