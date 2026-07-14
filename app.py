import streamlit as st
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="AI Resume Screening System",
    layout="centered"
)

# -----------------------------------
# TITLE
# -----------------------------------
st.title("AI Resume Screening System")
st.write("Upload a Resume and compare it with a Job Description")

# -----------------------------------
# FILE UPLOAD
# -----------------------------------
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# -----------------------------------
# JOB DESCRIPTION
# -----------------------------------
job_description = st.text_area(
    "Paste Job Description",
    height=200
)

# -----------------------------------
# PDF TEXT EXTRACTION
# -----------------------------------
def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + " "

    return text

# -----------------------------------
# MAIN LOGIC
# -----------------------------------
if uploaded_file and job_description:

    resume_text = extract_text(uploaded_file)

    # Text Similarity
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    # -----------------------------------
    # SKILLS DATABASE
    # -----------------------------------
    skills_database = [
        "python",
        "sql",
        "power bi",
        "excel",
        "aws",
        "machine learning",
        "deep learning",
        "data analysis",
        "tableau",
        "pandas",
        "numpy",
        "tensorflow",
        "streamlit",
        "flask",
        "scikit-learn",
        "opencv",
        "nlp",
        "github",
        "docker",
        "mongodb"
    ]

    resume_lower = resume_text.lower()
    jd_lower = job_description.lower()

    resume_skills = []
    jd_skills = []

    for skill in skills_database:

        if skill in resume_lower:
            resume_skills.append(skill)

        if skill in jd_lower:
            jd_skills.append(skill)

    matching_skills = sorted(
        list(set(resume_skills) & set(jd_skills))
    )

    missing_skills = sorted(
        list(set(jd_skills) - set(resume_skills))
    )

    # -----------------------------------
    # ATS SCORE
    # -----------------------------------
    if len(jd_skills) > 0:
        skill_match_percentage = (
            len(matching_skills) / len(jd_skills)
        ) * 100
    else:
        skill_match_percentage = 0

    final_score = round(
        (similarity * 40) +
        (skill_match_percentage * 0.60),
        2
    )

    # -----------------------------------
    # RESULTS
    # -----------------------------------
    st.divider()

    st.subheader("Resume Match Analysis")

    st.metric(
        label="ATS Match Score",
        value=f"{final_score}%"
    )

    st.progress(min(int(final_score), 100))

    if final_score >= 80:
        st.success("Excellent Match")
    elif final_score >= 60:
        st.success("Strong Match")
    elif final_score >= 40:
        st.warning("Moderate Match")
    else:
        st.error("Low Match")

    # -----------------------------------
    # SKILLS ANALYSIS
    # -----------------------------------
    st.divider()

    st.subheader("Skills Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.success("Matching Skills")

        if matching_skills:
            for skill in matching_skills:
                st.write(skill.title())
        else:
            st.write("No matching skills found")

    with col2:
        st.error("Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.write(skill.title())
        else:
            st.write("No missing skills")

    # -----------------------------------
    # SCORE BREAKDOWN
    # -----------------------------------
    st.divider()

    st.subheader("Score Breakdown")

    st.write(
        f"Text Similarity Score: {round(similarity * 100, 2)}%"
    )

    st.write(
        f"Skill Match Score: {round(skill_match_percentage, 2)}%"
    )

    # -----------------------------------
    # ATS RECOMMENDATION
    # -----------------------------------
    st.divider()

    st.subheader("ATS Recommendation")

    if final_score >= 80:
        st.success(
            "Excellent profile match. Highly recommended for this role."
        )

    elif final_score >= 60:
        st.info(
            "Good profile match. Consider adding more project experience."
        )

    elif final_score >= 40:
        st.warning(
            "Average profile match. Improve missing skills and strengthen your resume."
        )

    else:
        st.error(
            "Low profile match. Add relevant skills, certifications and projects."
        )

    # -----------------------------------
    # RESUME PREVIEW
    # -----------------------------------
    with st.expander("View Extracted Resume Text"):
        st.write(resume_text)