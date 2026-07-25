from skills import SKILLS


def extract_jd_skills(job_description):
    """
    Extract skills from the job description.
    """
    jd_text = job_description.lower()

    jd_skills = []

    for skill in SKILLS:
        if skill.lower() in jd_text:
            jd_skills.append(skill)

    return sorted(list(set(jd_skills)))


def match_resume_with_jd(resume_skills, jd_skills):
    """
    Compare resume skills with job description skills.
    """

    if not jd_skills:
        return 0, [], []

    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))

    match_score = int((len(matched) / len(jd_skills)) * 100)

    return match_score, matched, missing