
import pandas as pd
import re
from sentence_transformers import SentenceTransformer, util
import spacy
import streamlit as st

# Load Sentence-BERT model for semantic similarity
sbert_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Load spaCy for data preprocessing
preprocess_data = spacy.load('en_core_web_sm')

# Text Preprocessing Function
def preprocess_text(text):
    text = re.sub(r'[^\w\s]', ' ', text.lower())  # Remove non-word characters and convert to lowercase
    doc = preprocess_data(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]  # Lemmatization & stopword removal
    return " ".join(tokens)

# Load Sample Data (100 Resumes)
data = pd.read_csv(r"C:\Users\samru\Downloads\generated_resumes.csv")
data['cleaned_resume'] = data["Resume"].apply(preprocess_text)

# Load Job Descriptions
job_descriptions=({
    "Embedded Systems Engineer": "Experience in C, C++, microcontrollers, and real-time operating systems.",
    "Blockchain Developer": "Requires Solidity, Ethereum, smart contracts, and DeFi knowledge.",
    "IoT Engineer": "Building smart IoT systems using Raspberry Pi, MQTT, and cloud integration.",
    "Big Data Engineer": "Skills in Hadoop, Spark, and distributed computing systems required.",
    "Database Administrator": "Proficient in SQL, NoSQL, query optimization, and database security.",
    "NLP Engineer": "Expertise in text processing, sentiment analysis, and large language models.",
    "Robotics Engineer": "Experience in ROS, SLAM, and autonomous navigation systems.",
    "Computer Vision Engineer": "Proficient in OpenCV, deep learning for image processing, and object detection.",
    "Game Developer": "Looking for Unity/Unreal developers with experience in game physics and AI.",
    "AR/VR Developer": "Experience in immersive technologies using Unity3D, WebXR, and Oculus SDK.",
    "Bioinformatics Scientist": "Analyzing biological data using Python, R, and deep learning models.",
    "Data Analyst": "Requires skills in Power BI, Tableau, and statistical modeling.",
    "Business Intelligence Developer": "Expert in SQL, ETL pipelines, and business analytics.",
    "Marketing Analyst": "Analyzing customer data with Google Analytics, Excel, and marketing automation tools.",
    "SEO Specialist": "Expert in search engine optimization, keyword research, and Google Ads.",
    "Social Media Manager": "Experience in content strategy, social media analytics, and brand engagement.",
    "E-commerce Specialist": "Handling digital marketing, customer segmentation, and sales strategies.",
    "Product Manager": "Looking for a product leader with agile methodologies and customer research skills.",
    "UX/UI Designer": "Experience in Figma, Adobe XD, wireframing, and user experience research.",
    "Graphic Designer": "Proficient in Photoshop, Illustrator, and branding strategies.",
    "Technical Writer": "Seeking an expert in writing technical documentation, API docs, and blogs.",
    "Legal Consultant": "Expert in corporate law, intellectual property, and compliance management.",
    "HR Manager": "Skills in talent acquisition, employee engagement, and HR policies.",
    "Financial Analyst": "Proficient in stock market analysis, risk assessment, and financial modeling.",
    "Investment Banker": "Expert in M&A, venture capital, and financial instruments.",
    "Chartered Accountant": "Looking for an experienced CA specializing in taxation and auditing.",
    "Medical Data Scientist": "Combining healthcare analytics with machine learning for predictive diagnostics.",
    "Pharmaceutical Scientist": "Drug discovery research using bioinformatics and AI-driven screening.",
    "Energy Engineer": "Designing sustainable energy solutions for solar, wind, and hydro power projects.",
    "Civil Engineer": "Seeking an infrastructure planner skilled in CAD, structural analysis, and BIM.",
    "Mechanical Engineer": "Experience in product design, FEA analysis, and automotive engineering.",
    "Electrical Engineer": "Designing circuits, PCB layouts, and automation control systems.",
    "Aerospace Engineer": "Looking for an aerodynamics specialist with experience in aircraft design.",
    "Automotive Engineer": "Developing electric vehicle technology, ADAS, and powertrain systems.",
    "Supply Chain Analyst": "Skills in logistics optimization, inventory forecasting, and warehouse automation.",
    "Operations Manager": "Seeking an expert in business operations, lean methodologies, and cost efficiency.",
    "Public Relations Manager": "Proficient in media communications, brand management, and crisis handling.",
    "Event Planner": "Handling corporate events, logistics, and sponsorship partnerships.",
    "Customer Support Manager": "Managing service teams, CRM software, and customer retention strategies.",
    "Ethical Hacker": "Looking for a penetration testing expert skilled in cybersecurity tools and forensics.",
    "AI Ethics Researcher": "Studying fairness, bias mitigation, and responsible AI policies.",
    "Quantum Computing Researcher": "Expert in quantum algorithms, superconducting qubits, and QML.",
    "Autonomous Systems Engineer": "Developing self-driving technologies and robotic automation.",
    "Speech Recognition Engineer": "Building ASR models using deep learning and phonetics-based NLP.",
    "Hardware Engineer": "Experience in FPGA, circuit design, and semiconductor fabrication.",
    "Network Security Engineer": "Protecting networks using firewalls, IDS/IPS, and encryption.",
    "Systems Architect": "Designing scalable cloud architectures and enterprise solutions.",
    "Risk Management Consultant": "Assessing financial and operational risks for strategic planning.",
    "Food Scientist": "Researching food processing, safety, and nutritional innovations."
})

# Compute Semantic Similarity Function
def compute_similarity(job_description, resumes):
    job_embedding = sbert_model.encode(job_description, convert_to_tensor=True)  # Encode job description
    resume_embeddings = sbert_model.encode(resumes, convert_to_tensor=True)  # Encode resumes
    
    similarity_scores = util.cos_sim(job_embedding, resume_embeddings)  # Compute cosine similarity
    return similarity_scores.squeeze().cpu().numpy().tolist()  # Convert tensor to list


# Streamlit UI
st.title("🚀 AI-Powered Resume Parser")
st.sidebar.subheader("Select Job Title:")
job_title = st.sidebar.selectbox("Job Title", list(job_descriptions.keys()))

st.subheader("Job Description")
st.write(job_descriptions[job_title])

# Compute and Display Top Resumes
job_description = job_descriptions[job_title]
data['Similarity_Score'] = compute_similarity(job_description, data['cleaned_resume'].tolist())

top_resumes = data.sort_values(by='Similarity_Score', ascending=False).head(10)

st.subheader("Top Matching Resumes:")
for idx, row in enumerate(top_resumes.itertuples(), start=1):  # Fix indexing
    st.write(f"**Candidate {idx}: {row.Name}**")
    st.write(f"**Similarity Score:** {row.Similarity_Score:.2f}")
    st.write(f"**Resume:** {row.Resume}")
    st.write("---")
