# resume_parser
Project Overview:Recruiters often need to process hundreds of resumes to find the suitable candidates. Automating this process using AI can save time and effort and provide consistent results which manual screening might not be able to produce. This project analyses resumes to extract relevant info,evaluate candidates' skills and rank suitably.
<br>
<br>
<b>->Goals of the project:</b>
<br>
1)Automate resume screening:Extract relevant skills and qualifications from the resumes.
<br>
2)Evaluate context:Go beyond the keyword matching to understand the context.
<br>
3)Rank candidates:Assign scores to resumes indicating their fit for the job.
<br><br>
<b>->Libraries used</b>:NLTK, Pandas, Numpy, Skicit-learn, Spacy(For advanced nlp).
<br><br>
<b>->Workflow:</b>
<br>
1)Data preparation
<br> 2)Text pre-processing using Spacy.
<br>3)Compute Similarity using Sentence Bert from Sentence-Transformers.
<br>4)Sort the vectors according to similarity score.
<br>5)Create an interactive dashboard for user interface using streamlit.
<br><br>
<b>OUTPUT:</b>
List of first ten most eligible candidates for the job provided along with their resumes and similarity scores.
