print("✅ app.py started running")
from flask import Flask, render_template, request
from resume_matcher import extract_resume_text, calculate_similarity
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    if request.method == "POST":
        file = request.files["resume"]
        jd = request.form["job_desc"]

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        resume_text = extract_resume_text(file_path)
        score = calculate_similarity(resume_text, jd)

    return render_template("index.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)
