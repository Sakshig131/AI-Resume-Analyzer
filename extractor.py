import re


# -----------------------------
# Extract Email
# -----------------------------
def extract_email(text):
    """
    Extract email address from resume text.
    """
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


# -----------------------------
# Extract Phone Number
# -----------------------------
def extract_phone(text):
    """
    Extract Indian phone number.
    """

    pattern = r"(\+91[\-\s]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


# -----------------------------
# Extract LinkedIn
# -----------------------------
def extract_linkedin(text):
    """
    Extract LinkedIn profile link.
    """

    pattern = r"(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


# -----------------------------
# Extract GitHub
# -----------------------------
def extract_github(text):
    """
    Extract GitHub profile link.
    """

    pattern = r"(https?://)?(www\.)?github\.com/[A-Za-z0-9_-]+"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


# -----------------------------
# Resume Word Count
# -----------------------------
def word_count(text):
    """
    Count total words in resume.
    """

    return len(text.split())


# -----------------------------
# Resume Summary
# -----------------------------
def generate_summary(skills):
    """
    Generate a simple resume summary.
    """

    if not skills:
        return (
            "No technical skills were detected in the uploaded resume. "
            "Consider adding a dedicated Skills section."
        )

    skill_list = ", ".join(skills[:8])

    summary = (
        f"This resume demonstrates knowledge of {skill_list}. "
        f"A total of {len(skills)} technical skills were detected. "
        "The resume can be further improved by adding certifications, "
        "internship experience, measurable achievements, and a strong "
        "professional summary."
    )

    return summary