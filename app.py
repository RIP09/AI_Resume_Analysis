import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
import os

# Configure Gemini API (Use Secrets for Security)
genai.configure(api_key="YOUR_GEMINI_API_KEY")

def get_gemini_reponse(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        text += str(reader.pages[page].extract_text())
    return text

# UI Design
st.set_page_config(page_title="SmartRes AI Analyzer", layout="wide")
st.header("Code the Future: AI Resume Analyzer")
st.subheader("Improve your impact and align with Job Descriptions")

with st.sidebar:
    st.title("Settings")
    jd = st.text_area("Paste Target Job Description (JD)", help="Used for gap analysis")
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success("Resume Uploaded Successfully!")

# Prompt Logic for Evaluation Criteria [cite: 16, 19, 21]
input_prompt = """
As an experienced Technical Human Resource Manager, evaluate the provided resume against the JD. 
Provide:
1. A Rating (out of 10) for clarity and impact.
2. Extracted Highlights (Top 3 Skills & Projects).
3. 2-line Professional Summary.
4. Gap Analysis: List missing keywords/skills based on the JD.
5. Improvement Task: One specific action to reach a score of 8/10.
Format the output clearly using Markdown.
"""

if st.button("Analyze Resume"):
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)
        # In a real app, you'd pass resume_text and jd to the model
        response = get_gemini_reponse(input_prompt, [resume_text], jd)
        st.markdown("---")
        st.markdown(response)
    else:
        st.error("Please upload a resume first.")
