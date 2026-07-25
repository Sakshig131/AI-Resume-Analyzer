import streamlit as st
import pandas as pd
import plotly.express as px

from parser import extract_text
from scorer import (
    extract_skills,
    calculate_score,
    check_resume_sections,
    generate_suggestions,
)

from extractor import (
    extract_email,
    extract_phone,
    extract_linkedin,
    extract_github,
    word_count,
    generate_summary,
)

from jd_matcher import (
    extract_jd_skills,
    match_resume_with_jd,
)

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
)

st.title("📄 AI Resume Analyzer")
st.markdown("### Analyze your Resume and improve your ATS Score")

st.divider()

# ---------------------------------------------------
# FILE UPLOADS
# ---------------------------------------------------

resume_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

jd_file = st.file_uploader(
    "📝 Upload Job Description (.txt)",
    type=["txt"]
)

# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

if resume_file:

    # Extract Resume Text
    text = extract_text(resume_file)

    # Skills
    skills = extract_skills(text)

    # ATS Score
    score = calculate_score(text, skills)

    # Resume Sections
    sections = check_resume_sections(text)

    # Suggestions
    suggestions = generate_suggestions(text, skills)

    # Contact Details
    email = extract_email(text)
    phone = extract_phone(text)
    linkedin = extract_linkedin(text)
    github = extract_github(text)

    # Word Count
    total_words = word_count(text)

    # Resume Summary
    summary = generate_summary(skills)

    # ==========================================
    # ATS SCORE
    # ==========================================

    st.subheader("📊 ATS Resume Score")

    st.progress(score / 100)

    st.metric("ATS Score", f"{score}/100")

    st.divider()

    # ==========================================
    # CONTACT INFORMATION
    # ==========================================

    st.subheader("📞 Contact Information")

    c1, c2 = st.columns(2)

    with c1:
        st.write("📧 Email")
        st.success(email)

        st.write("📱 Phone")
        st.success(phone)

    with c2:
        st.write("💼 LinkedIn")
        st.info(linkedin)

        st.write("💻 GitHub")
        st.info(github)

    st.divider()

    # ==========================================
    # SKILLS & SECTIONS
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🧠 Detected Skills")

        if skills:
            for skill in skills:
                st.write("✅", skill.title())
        else:
            st.error("No Skills Found")

    with col2:

        st.subheader("📑 Resume Sections")

        for section, status in sections.items():
            if status:
                st.success(section)
            else:
                st.error(section)

    st.divider()

    # ==========================================
    # SKILL CHART
    # ==========================================

    if skills:

        df = pd.DataFrame({
            "Skill": skills,
            "Count": [1] * len(skills)
        })

        fig = px.bar(
            df,
            x="Skill",
            y="Count",
            title="Detected Technical Skills",
            text_auto=True
        )

        st.plotly_chart(fig, use_container_width=True)

    # ==========================================
    # JOB DESCRIPTION MATCHING
    # ==========================================

    if jd_file is not None:

        jd_text = jd_file.read().decode("utf-8")

        jd_skills = extract_jd_skills(jd_text)

        match_score, matched_skills, missing_skills = match_resume_with_jd(
            skills,
            jd_skills
        )

        st.divider()

        st.subheader("🎯 Resume vs Job Description Match")

        st.progress(match_score / 100)

        st.metric("Resume Match", f"{match_score}%")

        col3, col4 = st.columns(2)

        with col3:

            st.subheader("✅ Matched Skills")

            if matched_skills:
                for skill in matched_skills:
                    st.success(skill.title())
            else:
                st.warning("No Matching Skills Found")

        with col4:

            st.subheader("❌ Missing Skills")

            if missing_skills:
                for skill in missing_skills:
                    st.error(skill.title())
            else:
                st.success("Excellent! No Missing Skills.")

    st.divider()

    # ==========================================
    # RESUME DETAILS
    # ==========================================

    st.subheader("📄 Resume Details")

    st.write(f"**Total Words:** {total_words}")
    st.write(f"**Technical Skills Found:** {len(skills)}")
    st.write(f"**Completed Sections:** {sum(sections.values())}/5")

    st.divider()

    # ==========================================
    # AI SUMMARY
    # ==========================================

    st.subheader("🤖 AI Resume Summary")

    st.info(summary)

    st.divider()

    # ==========================================
    # SUGGESTIONS
    # ==========================================

    st.subheader("💡 Resume Improvement Suggestions")

    for suggestion in suggestions:
        st.write("✔", suggestion)

else:

    st.info("👆 Upload a Resume PDF to start analysis.")