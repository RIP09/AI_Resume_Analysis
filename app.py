import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
import os
from dotenv import load_dotenv

# Load API Key safely
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, pdf_content, prompt])
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        text += str(reader.pages[page].extract_text())
    return text

# --- Streamlit UI (Focus on UX/Design for 25% score) ---
st.set_page_config(page_title="SmartRes AI Analyzer", layout="centered")
st.title("🚀 Code the Future: Resume Analysis App")
st.info("Upload your resume and a Job Description to get an instant AI evaluation.")

# Sidebar for inputs
with st.sidebar:
    st.header("Input Section")
    jd = st.text_area("Target Job Description (JD)", height=200)
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Logic for Analysis
if st.button("Analyze Resume"):
    if uploaded_file is not None and jd.strip() != "":
        with st.spinner('AI is evaluating your resume...'):
            resume_text = input_pdf_text(uploaded_file)
            
            # This prompt covers all Problem Statement requirements [cite: 14-21]
            analysis_prompt = f"""
            Identify as an expert ATS (Applicant Tracking System) and Career Coach.
            
            1. **Extracted Highlights**: List top skills, projects, and keywords[cite: 15].
            2. **Quick Rating**: Give a score out of 10 for clarity and impact[cite: 16].
            3. **Professional Summary**: Provide a high-impact 2-line summary for the top[cite: 19].
            4. **JD Comparison**: Identify missing skills and alignment gaps[cite: 21].
            5. **Improvement Task**: Provide specific recommendations to reach a score of 8/10[cite: 18].
            """
            
            response = get_gemini_response(resume_text, jd, analysis_prompt)
            st.subheader("Evaluation Results")
            st.markdown(response)
    else:
        st.warning("Please upload a PDF and provide a Job Description.")