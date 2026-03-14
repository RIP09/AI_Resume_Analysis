import streamlit as st
from google import genai  # NEW IMPORT
import PyPDF2 as pdf
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize the new Client
client = genai.Client(api_key=api_key) 

def get_gemini_response(resume_text, jd, prompt):
    # The new library makes it much simpler to call the model
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", # Use the latest stable model
            contents=f"{prompt}\n\nResume:\n{resume_text}\n\nJD:\n{jd}"
        )
        return response.text
    except Exception as e:
        return f"AI Error: {str(e)}"

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        text += str(reader.pages[page].extract_text())
    return text

# 2. UI CODE
st.set_page_config(page_title="SmartRes AI", layout="centered")
st.title("🚀 Code the Future: AI Resume Analyzer")

jd = st.text_area("Paste Job Description (JD)")
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if st.button("Analyze Resume"):
    if uploaded_file and jd:
        with st.spinner('AI is evaluating...'):
            resume_text = input_pdf_text(uploaded_file)
            analysis_prompt = """
            As an expert Recruiter, provide:
            1. Resume Rating (out of 10).
            2. Extracted Highlights (Skills/Projects).
            3. A STRICTLY 2-LINE Professional Summary.
            4. Gap Analysis (Missing skills from JD).
            5. Improvement Task to reach 8/10 score.
            """
            result = get_gemini_response(resume_text, jd, analysis_prompt)
            st.markdown(result)
    else:
        st.error("Missing Resume or JD.")
