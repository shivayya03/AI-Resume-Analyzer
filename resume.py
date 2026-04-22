import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from skills_db import smart_suggestions, generate_feedback


# Load BERT Model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Page Config
st.set_page_config(page_title="AI Resume Analyzer (BERT)", page_icon="📄")


# Extract text from PDF

def extract_text(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text


# Match score using BERT

def match_score(resume, job_desc):
    embeddings = model.encode([resume, job_desc])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])
    return score[0][0] * 100



# UI

st.title("📄 AI Resume Analyzer (BERT)")
st.markdown("### 🔥 Semantic Matching using BERT")

uploaded_file = st.file_uploader("Upload Resume (PDF) ", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if uploaded_file and job_desc:
        with st.spinner("Analyzing with BERT..."):
            resume_text = extract_text(uploaded_file)
            score = match_score(resume_text, job_desc)

        st.success(f"Match Score: {score:.2f}%")
        st.progress(int(score))

        # Suggestions
        suggestions = smart_suggestions(resume_text, job_desc)

        st.subheader("🤖 AI Suggestions")
        if suggestions:
            for s in suggestions:
                st.write(f"• Add skill: {s}")
        else:
            st.success("Your resume is well aligned!")
        st.markdown("## 🤖 Detailed AI Feedback")

        feedback = generate_feedback(resume_text, job_desc, score, suggestions)

        for f in feedback:
          st.write(f"👉 {f}")
    else:
        st.error("Upload resume and enter job description")

st.markdown("---")
st.markdown("Built with ❤️ using BERT | Shivayya")