import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
import os
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 2. Function to Extract Text from PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        text += str(reader.pages[page].extract_text())
    return text

# 3. AI Response Function
def get_gemini_reponse(input_prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(input_prompt)
    return response.text

# 4. Streamlit UI (Meets User Experience Criteria)
st.set_page_config(page_title="SmartRes AI Analyzer", page_icon="📄")
st.title("Code the Future: AI Resume Analyzer")
st.markdown("### Unfold success from untold experiences")

# Inputs
jd = st.text_area("Paste the Target Job Description (JD) here...")
uploaded_file = st.file_uploader("Upload your Resume (PDF)...", type=["pdf"])

if st.button("Analyze My Resume"):
    if uploaded_file is not None and jd != "":
        with st.spinner('Analyzing your resume against the JD...'):
            # Extract text
            resume_content = input_pdf_text(uploaded_file)
            
            # Refined Prompt to cover all Problem Statement requirements
            prompt = f"""
            Role: Expert Resume Critic and Career Coach.
            Target JD: {jd}
            Resume Content: {resume_content}

            Please provide the following in structured Markdown:
            1. **Extracted Highlights**: List key skills and top projects found in the resume.
            2. **Resume Rating**: Provide a score out of 10 for clarity and impact.
            3. **Professional Summary**: A high-impact 2-line summary for the top of the resume.
            4. **JD Comparison**: Identify missing skills and alignment gaps compared to the JD.
            5. **Improvement Plan**: Specific tasks to improve the score to at least 8/10.
            """
            
            response = get_gemini_reponse(prompt)
            st.subheader("Analysis Results")
            st.markdown(response)
    else:
        st.error("Please provide both a Job Description and a Resume PDF.")
