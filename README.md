
---

### README.md Content

```markdown
# 🚀 SmartRes AI - Professional Resume Analyzer

**SmartRes AI** is a high-performance career tool built for the **UnsaidTalks: Code the Future** hackathon. It leverages Google Gemini 1.5 Flash to provide deep, recruiter-level insights into how well a resume matches a Job Description.

## 🌟 Key Features
- **ATS-Style Scoring:** Instant rating out of 10 based on JD relevance.
- **Strict 2-Line Summary:** High-impact professional summaries designed to pass human screening.
- **Skill Gap Analysis:** Highlights specific missing keywords and technologies.
- **Actionable Task:** Provides a single, high-priority task to improve the resume score to 8/10 or higher.
- **Smart Model Fallback:** Built-in technical redundancy to ensure uptime.

## 🛠️ Installation & Setup
To run this project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RIP09/resumeanalyzer-ai.git
   cd resumeanalyzer-ai

```

2. **Create a Virtual Environment (Recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


4. **Setup Environment Variables:**
* Create a file named `.env` in the root directory.
* Add your Google API Key:
```text
GOOGLE_API_KEY=your_actual_api_key_here

```





## 🚦 Usage

1. Start the Streamlit server:
```bash
streamlit run app.py

```


2. Open your browser to `http://localhost:8501`.
3. Paste the **Job Description** in the text area.
4. Upload your **Resume (PDF)**.
5. Click **"Analyze Resume"** to receive AI-powered feedback.

## 🏗️ Technical Execution

* **Core Logic:** Python & Streamlit
* **LLM:** Google Gemini API (Flash/Pro)
* **PDF Parsing:** PyPDF2
* **Environment Management:** Python-Dotenv

```

---

