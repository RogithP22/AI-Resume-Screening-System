# AI Resume Screening System

An AI-powered Resume Screening System built using Python, Streamlit, and Natural Language Processing (NLP) techniques to compare resumes against job descriptions and generate ATS-style recommendations.

[Live Demo](https://ai-resume-screening-system-r9fjvzgwfnoxyfyl8c68qu.streamlit.app/)

---

## Overview

The AI Resume Screening System helps job seekers evaluate how well their resume matches a given job description.

The application extracts text from uploaded PDF resumes, analyzes the content using NLP techniques, identifies matching and missing skills, and generates an ATS Match Score.

---

## Features

- Upload Resume in PDF format
- Extract resume text automatically
- Compare resume with job description
- Calculate ATS Match Score
- Identify matching skills
- Identify missing skills
- Generate ATS recommendations
- Display score breakdown
- View extracted resume text

---

## Technologies Used

- Python
- Streamlit
- PyPDF2
- Scikit-Learn
- TF-IDF Vectorization
- Cosine Similarity
- NLP Techniques

---

## Project Workflow

1. User uploads a PDF resume.
2. User enters a job description.
3. Resume text is extracted using PyPDF2.
4. TF-IDF Vectorization converts text into numerical features.
5. Cosine Similarity measures resume-job similarity.
6. Skills are extracted and compared.
7. ATS Match Score is generated.
8. Recommendations are displayed.

---

## Project Structure

```text
AI-Resume-Screening-System
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/RogithP22/AI-Resume-Screening-System.git
```

Move into the project folder:

```bash
cd AI-Resume-Screening-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

---

## Sample Skills Supported

- Python
- SQL
- Power BI
- Excel
- AWS
- Machine Learning
- Deep Learning
- Data Analysis
- Tableau
- Pandas
- NumPy
- TensorFlow
- Streamlit
- Flask
- OpenCV
- NLP
- GitHub
- Docker
- MongoDB

---

## ATS Score Calculation

The final ATS score is calculated using:

- Text Similarity Score
- Skill Match Percentage

Formula:

```text
Final ATS Score =
(0.4 × Text Similarity Score)
+
(0.6 × Skill Match Score)
```

---

## Future Enhancements

- Resume Ranking System
- Multiple Resume Comparison
- AI-Powered Resume Suggestions
- PDF Report Generation
- Interactive Dashboard
- Advanced NLP Models (BERT/Sentence Transformers)
- Resume Improvement Recommendations

---

## Live Application

https://ai-resume-screening-system-r9fjvzgwfnoxyfyl8c68qu.streamlit.app/

---

## GitHub Repository

https://github.com/RogithP22/AI-Resume-Screening-System

---

## Author

**Rogith P**

B.Tech Artificial Intelligence and Data Science  
PSNA College of Engineering and Technology

LinkedIn: https://www.linkedin.com/in/rogith-p-b01899341

---

## License

This project is developed for educational and portfolio purposes.