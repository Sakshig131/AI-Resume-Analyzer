from skills import SKILLS


# -----------------------------
# Extract Skills
# -----------------------------
def extract_skills(text):
    """
    Detect technical skills from resume.
    """
    found_skills = []

    text = text.lower()

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


# -----------------------------
# ATS Score
# -----------------------------
def calculate_score(text, skills):

    score = 0

    # -------------------------
    # Skills (40 Marks)
    # -------------------------
    skill_score = min(len(skills) * 4, 40)
    score += skill_score

    # -------------------------
    # Resume Sections (40 Marks)
    # -------------------------
    sections = {
        "education": 8,
        "skills": 8,
        "projects": 8,
        "experience": 8,
        "certifications": 8,
    }

    text = text.lower()

    for section, marks in sections.items():
        if section in text:
            score += marks

    # -------------------------
    # Contact Information (10 Marks)
    # -------------------------
    if "@" in text:
        score += 5

    if any(char.isdigit() for char in text):
        score += 5

    # -------------------------
    # Resume Length (10 Marks)
    # -------------------------
    words = len(text.split())

    if words >= 300:
        score += 10
    elif words >= 200:
        score += 7
    elif words >= 100:
        score += 5

    return min(score, 100)


# -----------------------------
# Resume Sections
# -----------------------------
def check_resume_sections(text):

    text = text.lower()

    sections = {
        "Education": "education" in text,
        "Skills": "skills" in text,
        "Projects": "project" in text,
        "Experience": "experience" in text,
        "Certifications": (
            "certification" in text
            or "certifications" in text
            or "certificate" in text
        ),
    }

    return sections


# -----------------------------
# Suggestions
# -----------------------------
def generate_suggestions(text, skills):

    suggestions = []

    sections = check_resume_sections(text)

    if len(skills) < 8:
        suggestions.append(
            "Add more technical skills relevant to your target job."
        )

    if not sections["Projects"]:
        suggestions.append(
            "Include at least 2-3 academic or personal projects."
        )

    if not sections["Experience"]:
        suggestions.append(
            "Mention internships, freelancing, or practical experience."
        )

    if not sections["Certifications"]:
        suggestions.append(
            "Add certifications from Coursera, Udemy, NPTEL, or Google."
        )

    if "github" not in text:
        suggestions.append(
            "Add your GitHub profile link."
        )

    if "linkedin" not in text:
        suggestions.append(
            "Add your LinkedIn profile link."
        )

    if "objective" not in text and "summary" not in text:
        suggestions.append(
            "Include a professional career objective or summary."
        )

    if len(text.split()) < 200:
        suggestions.append(
            "Your resume is too short. Try adding more relevant content."
        )

    if not suggestions:
        suggestions.append(
            "Excellent! Your resume covers most ATS requirements."
        )

    return suggestions