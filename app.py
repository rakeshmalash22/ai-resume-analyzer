import streamlit as st
from analyzer import analyze_resume
from parser import extract_text_from_pdf

st.title("🚀 AI Resume Analyzer + Job Matcher")

uploaded_file = st.file_uploader("Upload Resume (PDF/TXT)", type=["pdf","txt"])
job_desc = st.text_area("Paste Job Description")

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        resume_text = extract_text_from_pdf(uploaded_file)
    else:
        resume_text = uploaded_file.read().decode("utf-8")

    st.write(resume_text[:1000])

    if st.button("Analyze"):
        result = analyze_resume(resume_text, job_desc)
        st.write(result)
