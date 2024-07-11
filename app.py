import pandas as pd
import streamlit as st
from groq import Groq
import os
import time
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('GROQ_API_KEY')
client = Groq(
    api_key=API_KEY,
)

holdings = pd.read_csv(r'data\holdings.csv')
trades = pd.read_csv(r'data\trades.csv')

holdings.fillna(0, inplace=True)
trades.fillna(0, inplace=True)

def generate_prompt(question):
    holdings_sample = holdings.sample(n=25).to_string(index=False)  
    trades_sample = trades.sample(n=25).to_string(index=False)  
    
    prompt = f"""
    You are a financial chatbot. Answer the question based on the data provided in the CSV files.

    Sample of Holdings data:
    {holdings_sample}

    Sample of Trades data:
    {trades_sample}

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

question = st.text_input("Hey, You can ask me anything about Proprty Deals made through PropertyLoop !!")

if question:
    prompt = generate_prompt(question)
    answer = get_groq_response(prompt)
    st.write(answer)

latest_iteration = st.empty()
