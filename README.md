
```markdown
# 🚀 SmartRes AI: Professional Resume Analyzer

**SmartRes AI** is an intelligent career tool designed to bridge the gap between job seekers and recruiters. Built for the **UnsaidTalks: Code the Future** hackathon, it leverages the **Google Gemini 1.5 Flash** model to provide deep, recruiter-level insights.

## 🌟 Key Features
- **ATS-Style Scoring:** Instant rating out of 10 based on JD relevance.
- **Strict 2-Line Summary:** Generates high-impact professional summaries designed to pass human screening.
- **Skill Gap Analysis:** Highlights specific missing keywords and technologies required by the JD.
- **Actionable Task:** Provides a single, high-priority "Improvement Task" to help the user reach a score of 8/10.
- **Smart Model Fallback:** Built-in technical redundancy to ensure stability across different Gemini API versions.

## 🏗️ Technical Stack
- **Frontend:** [Streamlit](https://streamlit.io/)
- **AI Engine:** [Google Gemini API](https://ai.google.dev/)
- **PDF Processing:** [PyPDF2](https://pypdf2.readthedocs.io/)
- **Language:** Python 3.9+

---

## 🛠️ Installation & Setup

To run this project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/RIP09/resumeanalyzer-ai.git
cd resumeanalyzer-ai

```

### 2. Install Dependencies

Make sure you have Python installed, then run:

```bash
pip install streamlit google-generativeai PyPDF2 python-dotenv

```
```
# Step A: Ensure pip is up to date
python -m pip install --upgrade pip

# Step B: Install the necessary tools (Fixed command)
python -m pip install streamlit google-generativeai PyPDF2 python-dotenv
```
### 3. Configure API Credentials

Create a `.env` file in the root directory and add your Google API Key:

env

GOOGLE_API_KEY=your_api_key_here



### 4. Run the Application

```bash
streamlit run app.py

```

---

## 🚦 How to Use

1. **Upload:** Drop your resume in PDF format into the uploader.
2. **Input:** Paste the Job Description you are targeting in the text area.
3. **Analyze:** Click the **"Analyze Resume"** button.
4. **Iterate:** Review the **Gap Analysis** and perform the **Improvement Task** suggested by the AI to boost your score.

## 🛡️ Security Note

This project uses `.env` files to manage API keys. Ensure the `.env` file is included in your `.gitignore` to prevent leaking credentials to public repositories.

---

**Developed for the UnsaidTalks Hackathon | March 2026**

```
```
Developed by Deepanshu Murmu
For Code the Future: AI Edition Hackathon
---

