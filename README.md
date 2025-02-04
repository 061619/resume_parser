<b><u>AI-Powered Resume Screening System</u></b>
<br><br>
<br><b> Project Overview</b>
<br><br>
Recruiters
often need to process hundreds (or even thousands) of resumes to find the best candidates for a job. Manually screening each resume is time-consuming, subjective, and prone to inconsistencies. To solve this challenge, our AI-powered resume screening system automates the process using Natural Language Processing (NLP) and Machine Learning (ML). This system efficiently extracts relevant information, evaluates candidates' skills based on job descriptions, and ranks resumes according to their suitability.
<br><br>
By leveraging state-of-the-art NLP models, this project aims to go beyond simple keyword matching and understand the contextual meaning of resumes, ensuring accurate and fair candidate selection.
<br><br>
<b>Goals of the Project</b>
<br><br>
1)Automate Resume Screening: Extract relevant skills, qualifications, and experiences from resumes using NLP techniques.
<br><br>
2) Evaluate Contextual Relevance: Move beyond basic keyword matching by using advanced NLP techniques to understand the true meaning of resumes and job descriptions.
<br><br>
3)Rank Candidates Based on Suitability: Assign similarity scores to resumes based on their alignment with job descriptions, ensuring the most relevant candidates appear at the top.
<br><br>
4)User-Friendly Interface: Develop an interactive dashboard using Streamlit to allow recruiters to upload job descriptions and resumes, view ranked candidates, and download the results.
<br><br>
<b> Technologies & Libraries Used</b>
<br><br>
Python: The core programming language for development.
<br><br>
NLTK: For basic text processing and tokenization.
<br><br>
spaCy: For advanced NLP techniques like Named Entity Recognition (NER) and dependency parsing.
<br><br>
Pandas & NumPy: For data manipulation and numerical computations.
<br><br>
scikit-learn: For machine learning models and similarity computation.
<br><br>
Sentence-BERT (Sentence-Transformers): For computing semantic similarity between resumes and job descriptions.
<br><br>
Streamlit: For building an interactive and user-friendly dashboard.
<br><br>
<b>Workflow & Methodology</b>
<br><br>
1)Data Collection & Preprocessing:
<br>
-Parse resumes (PDF/DOCX) and extract text.
<br>
-Clean and normalize text (lowercasing, stopword removal, lemmatization).
<br>
-Extract relevant information such as skills, education, experience, and contact details.
<br><br>
2)Text Processing & Feature Engineering:
<br>
-Use spaCy for Named Entity Recognition (NER) to extract key information.
<br>
-Tokenize, remove stopwords, and lemmatize text for better understanding.
<br>
-Convert processed text into vector representations.
<br><br>
3)Computing Semantic Similarity:
<br>
-Use Sentence-BERT (SBERT) to generate high-quality embeddings for both resumes and job descriptions.
<br>
-Compute cosine similarity between each resume and the given job description.
<br><br>
4)Ranking Candidates:
<br>
-Sort resumes based on their similarity scores.
<br>
-Display the top 10 most relevant resumes for the job description.
<br><br>
5)Interactive Dashboard with Streamlit:
<br>
-Allow recruiters to upload job descriptions and resume files.
<br>
-Display ranked resumes along with similarity scores.
<br><br>

<b>Expected Output</b>
<br>
The system will output a ranked list of the top 10 most suitable candidates for a given job description. Each resume will be assigned a similarity score, allowing recruiters to quickly identify the best matches. The dashboard will display the candidates’ key details, extracted skills, and a link to their resumes.

