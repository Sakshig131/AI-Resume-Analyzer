# 📄 AI Resume Analyzer

An AI-powered ATS (Applicant Tracking System) Resume Analyzer built using **Python and Streamlit**.  
This application analyzes resumes, calculates ATS scores, extracts important information, detects skills, and compares resumes with job descriptions.

---

# 🚀 Features

## 📌 Resume Analysis

- Upload resume in PDF format
- Extract resume text automatically
- Clean and process resume content
- Calculate ATS compatibility score

## 📊 ATS Resume Scoring

The system evaluates resumes based on:

- Technical skills
- Resume sections
- Education
- Projects
- Experience
- Certifications
- Contact information
- Resume length

Output:

```
ATS Score: 85/100
```

---

## 🧠 Skill Detection

Automatically detects technical skills from resumes.

Examples:

- Python
- Java
- SQL
- Machine Learning
- Power BI
- Excel
- TensorFlow
- AWS
- Docker
- Git
- React

---

## 📞 Personal Information Extraction

Extracts:

- Email address
- Phone number
- LinkedIn profile
- GitHub profile

---

## 📑 Resume Section Analysis

Checks important resume sections:

✅ Education  
✅ Skills  
✅ Projects  
✅ Experience  
✅ Certifications  

---

## 🎯 Job Description Matching

Compare resume skills with job requirements.

Features:

- Upload job description
- Calculate resume-job match percentage
- Find matching skills
- Identify missing skills

Example:

```
Resume Match: 78%

Matched Skills:
✓ Python
✓ SQL
✓ Excel

Missing Skills:
✗ AWS
✗ Docker
```

---

## 💡 Resume Improvement Suggestions

Provides recommendations such as:

- Add more technical skills
- Include projects
- Add certifications
- Add LinkedIn/GitHub links
- Improve resume content

---

# 🛠️ Tech Stack

## Programming Language

- Python

## Framework

- Streamlit

## Libraries

- pdfplumber → PDF text extraction
- Pandas → Data processing
- Plotly → Data visualization
- Regex → Information extraction

---

# 📂 Project Structure

```
AI-Resume-Analyzer/

│
├── app.py              # Streamlit application
├── parser.py           # PDF text extraction
├── scorer.py           # ATS score calculation
├── skills.py           # Skills database
├── extractor.py        # Email, phone, LinkedIn, GitHub extraction
├── jd_matcher.py       # Resume and job description matching
├── requirements.txt    # Required libraries
└── README.md           # Project documentation
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/Sakshig131/AI-Resume-Analyzer.git
```

## 2. Navigate to Project Folder

```bash
cd AI-Resume-Analyzer
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run Application

```bash
streamlit run app.py
```

---

# 📸 Application Workflow

```
Upload Resume PDF

        ↓

Extract Resume Text

        ↓

Detect Skills

        ↓

Calculate ATS Score

        ↓

Analyze Resume Sections

        ↓

Compare Job Description

        ↓

Generate Suggestions
```

---

# 🎯 Future Improvements

Future versions can include:

- AI-generated resume rewriting
- Deep learning based skill extraction
- Resume ranking system
- Multiple resume comparison
- PDF report generation
- Cloud deployment
- Database integration
- User authentication

---

# 👨‍💻 Author

**Sakshi**

AI Resume Analyzer Project

---

# ⭐ Support

If you find this project useful, consider giving it a star ⭐ on GitHub.
