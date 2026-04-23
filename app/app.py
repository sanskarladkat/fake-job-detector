import os
import sys
from pathlib import Path

# ✅ Fix import issue (Streamlit + src folder)
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
from src.predict import predict_job

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Fake Job Detector",
    layout="wide",
    page_icon="🧠"
)

# -------------------- HEADER --------------------
st.markdown("<h1 style='text-align: center;'>🧠 Fake Job Detection System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Detect suspicious job postings using Machine Learning</p>", unsafe_allow_html=True)

# -------------------- SIDEBAR INPUT --------------------
st.sidebar.header("📌 Enter Job Details")

job_title = st.sidebar.text_input("Job Title")
job_desc = st.sidebar.text_area("Job Description")
requirements = st.sidebar.text_area("Requirements")

analyze = st.sidebar.button("🔍 Analyze Job")

# -------------------- MAIN LAYOUT --------------------
col1, col2 = st.columns([2, 1])

full_text = f"{job_title} {job_desc} {requirements}".strip()

# -------------------- LEFT SIDE --------------------
with col1:
    st.subheader("📄 Job Description Preview")

    if full_text:
        st.write(full_text)
    else:
        st.info("Enter job details from sidebar...")

# -------------------- RIGHT SIDE --------------------
with col2:
    st.subheader("📊 Prediction Result")

    if analyze:
        if not full_text:
            st.warning("⚠️ Please enter job details first")
        else:
            try:
                prob, risk = predict_job(full_text)

                # 🎨 Color Logic
                if "HIGH" in risk:
                    color = "red"
                elif "MEDIUM" in risk:
                    color = "orange"
                else:
                    color = "green"

                # 📊 Metrics
                st.metric(label="Fake Probability", value=f"{round(prob * 100, 2)}%")
                st.markdown(
                    f"<h3 style='color:{color};'>Risk Level: {risk}</h3>",
                    unsafe_allow_html=True
                )

                # -------------------- EXPLANATION --------------------
                st.markdown("---")
                st.subheader("🧠 Why this job is flagged?")

                reasons = []

                text_lower = full_text.lower()

                if "no experience" in text_lower:
                    reasons.append("⚠️ Contains 'No Experience' keyword")

                if "urgent" in text_lower:
                    reasons.append("⚠️ Uses urgency words (common in scams)")

                if len(full_text) < 50:
                    reasons.append("⚠️ Very short description")

                if prob > 0.7:
                    reasons.append("⚠️ Model strongly predicts fraud")

                if not reasons:
                    reasons.append("✅ No major suspicious patterns detected")

                for r in reasons:
                    st.write(r)

            except Exception as e:
                st.error("❌ Error during prediction")
                st.exception(e)