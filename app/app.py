import os
import sys
from pathlib import Path

# Ensure the project root is on sys.path so imports work when running from app/
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
from src.predict import predict_job

st.set_page_config(page_title="Fake Job Detector", layout="wide")

# HEADER
st.markdown("<h1 style='text-align: center;'>🧠 Fake Job Detection System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Detect suspicious job postings using Machine Learning</p>", unsafe_allow_html=True)


st.sidebar.header("📌 Enter Job Details")

job_title = st.sidebar.text_input("Job Title")
job_desc = st.sidebar.text_area("Job Description")
requirements = st.sidebar.text_area("Requirements")

analyze = st.sidebar.button("🔍 Analyze Job")


col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📄 Job Description Preview")
    full_text = job_title + " " + job_desc + " " + requirements
    st.write(full_text if full_text.strip() != "" else "Enter job details from sidebar...")

with col2:
    st.subheader("📊 Prediction Result")

    if analyze:
        prob, risk = predict_job(full_text)

        
        if "HIGH" in risk:
            color = "red"
        elif "MEDIUM" in risk:
            color = "orange"
        else:
            color = "green"

        
        st.metric(label="Fake Probability", value=f"{round(prob*100, 2)}%")
        st.markdown(f"<h3 style='color:{color};'>Risk Level: {risk}</h3>", unsafe_allow_html=True)


        st.markdown("---")
        st.subheader("🧠 Why this job is flagged?")

        reasons = []

        if "no experience" in full_text.lower():
            reasons.append("⚠️ Contains 'No Experience' keyword")

        if "urgent" in full_text.lower():
            reasons.append("⚠️ Uses urgency words (common in scams)")

        if len(full_text) < 50:
            reasons.append("⚠️ Very short description")

        if prob > 0.7:
            reasons.append("⚠️ Model strongly predicts fraud")

        if len(reasons) == 0:
            reasons.append("✅ No major suspicious patterns detected")

        for r in reasons:
            st.write(r)