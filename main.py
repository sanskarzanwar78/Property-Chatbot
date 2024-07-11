import pandas as pd
import streamlit as st
from groq import Groq
from sentence_transformers import SentenceTransformer
import faiss
from dotenv import load_dotenv
import numpy as np
import os

load_dotenv()
API_KEY = os.getenv('GROQ_API_KEY')

client = Groq(api_key=API_KEY)

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def load_csv_files(folder_path):
    csv_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]
    data_frames = [pd.read_csv(file) for file in csv_files]
    return data_frames

folder_path = 'data'
data_frames = load_csv_files(folder_path)

def preprocess_data(df):
    df['text'] = df.apply(lambda row: ' '.join(row.astype(str)), axis=1)
    return df['text'].tolist()

texts = []
for df in data_frames:
    texts.extend(preprocess_data(df))

embeddings = model.encode(texts)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings, dtype=np.float32))

def retrieve_relevant_data(question, top_n=5):
    question_embedding = model.encode([question])
    _, indices = index.search(np.array(question_embedding, dtype=np.float32), top_n)
    return [texts[i] for i in indices[0]]

def generate_prompt(question):
    relevant_data = retrieve_relevant_data(question)
    relevant_data_text = '\n'.join(relevant_data)
    
    prompt = f"""
    You are a financial chatbot. Answer the question based on the data provided in the CSV files.

    Relevant data:
    {relevant_data_text}

    Question: {question}
    """
    return prompt


def get_groq_response(prompt):
    chat = client.chat.completions.create(
    messages=[
        {"role": "system",
        "content": """
        You are a Property chatbot designed to assist users with their Property inquiries. Your primary task is to answer questions based on the provided holdings and trades data. 

        - Always reference the provided data in your responses.
        - Provide clear, concise, and accurate answers.
        - If the question involves data interpretation, explain your reasoning based on the data.
        - Maintain a professional and informative tone.
        - If you don't have sufficient data to answer a question, acknowledge this and suggest the user provide more specific details.

        The data you will be using includes information about users' holdings and recent trades. Use this data to provide insights, summaries, and relevant property advice.
        """},
        {"role": "user", "content": prompt},
    ],
    model="llama3-70b-8192",
    n=1,
    stop=None,
    temperature=0.7,
    )
    return chat.choices[0].message.content

st.title('Property Data Chatbot')

question = st.text_input("Hey, You can ask me anything about Property Deals made through PropertyLoop !!")

if question:
    prompt = generate_prompt(question)
    answer = get_groq_response(prompt)
    st.write(answer)
