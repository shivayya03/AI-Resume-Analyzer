skills_db = [
    # Programming Languages
    "python", "java", "c++", "c", "sql", "javascript", "r",

    # Data Science & Analysis
    "data analysis", "data visualization", "exploratory data analysis", "eda",
    "pandas", "numpy", "matplotlib", "seaborn", "plotly",

    # Machine Learning
    "machine learning", "supervised learning", "unsupervised learning",
    "regression", "linear regression", "logistic regression",
    "classification", "decision trees", "random forest", "xgboost",
    "clustering", "k-means", "knn", "svm",

    # NLP (Natural Language Processing)
    "nlp", "natural language processing", "text processing",
    "tokenization", "stemming", "lemmatization",
    "tf-idf", "bag of words", "word embeddings",
    "bert", "transformers", "text classification", "sentiment analysis",

    # Deep Learning
    "deep learning", "neural networks", "artificial neural networks",
    "cnn", "convolutional neural networks",
    "rnn", "recurrent neural networks",
    "lstm", "gru",

    # Frameworks & Libraries
    "scikit-learn", "tensorflow", "pytorch", "keras", "huggingface",

    # Data Engineering / Big Data
    "hadoop", "spark", "pyspark", "data pipelines", "etl",

    # Databases
    "mysql", "postgresql", "mongodb", "nosql",

    # Tools & Platforms
    "excel", "power bi", "tableau",
    "git", "github", "docker", "kubernetes",

    # Cloud Platforms
    "aws", "azure", "google cloud", "gcp",

    # MLOps / Deployment
    "model deployment", "mlops", "flask", "fastapi", "streamlit",
    "api development", "ci/cd",

    # Concepts
    "feature engineering", "data preprocessing",
    "model evaluation", "cross validation",
    "hyperparameter tuning", "bias variance",
    "overfitting", "underfitting"
]

def smart_suggestions(resume, job_desc):
    resume = resume.lower()
    job_desc = job_desc.lower()

    missing = []
    for skill in skills_db:
        if skill in job_desc and skill not in resume:
            missing.append(skill)

    return missing


def generate_feedback(resume, job_desc, score, missing_skills):
    feedback = []

    # -------------------------
    # Overall Feedback
    # -------------------------
    if score < 50:
        feedback.append("Your resume currently does not align well with the job requirements. You should significantly improve both skills and project relevance.")
    elif score < 80:
        feedback.append("Your resume shows moderate alignment with the job role, but there are important areas that need improvement.")
    else:
        feedback.append("Your resume is well aligned with the job description. Only minor improvements are needed.")

    # -------------------------
    # Missing Skills Explanation
    # -------------------------
    if missing_skills:
        skill_text = ", ".join(missing_skills[:5])
        feedback.append(f"The job description emphasizes skills like {skill_text}, but these are missing or not clearly mentioned in your resume.")
        feedback.append("You should include these skills in your Skills section or demonstrate them through projects and experience.")

    # -------------------------
    # Project Suggestions
    # -------------------------
    if "project" not in resume.lower():
        feedback.append("Your resume lacks strong project evidence. Consider adding 1–2 real-world projects that demonstrate your practical knowledge.")

    # -------------------------
    # Achievement Suggestions
    # -------------------------
    if "%" not in resume:
        feedback.append("Your resume does not include measurable achievements. Add metrics such as 'improved accuracy by 20%' or 'processed 5000+ records'.")

    # -------------------------
    # Keyword Optimization
    # -------------------------
    feedback.append("Ensure that important keywords from the job description are naturally included in your resume, especially in Skills and Experience sections.")

    # -------------------------
    # Language Improvement
    # -------------------------
    feedback.append("Use strong action verbs like 'Developed', 'Built', 'Optimized' instead of weak phrases like 'Worked on' or 'Responsible for'.")

    return feedback