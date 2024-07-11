# import tempfile
# import streamlit as st
# from dotenv import load_dotenv
# from langchain.chains import RetrievalQA
# from langchain.document_loaders.csv_loader import CSVLoader
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.llms import OpenAI
# from langchain.vectorstores import DocArrayInMemorySearch
# import pandas as pd
# from groq import Groq
# import os
# from sentence_transformers import SentenceTransformer
# from chromadb import Chroma
# from chromadb.config import Settings


# load_dotenv()

# API_KEY = os.getenv('GROQ_API_KEY')
# client = Groq(
#     api_key=API_KEY,# "Gjjnmfko"
# )

# folder_path = 'data'

# def load_csv_files(folder_path):
#     csv_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]
#     data_frames = [pd.read_csv(file) for file in csv_files]
#     return data_frames

# data_frames = load_csv_files(folder_path)
# # holdings = pd.read_csv('holdings.csv')
# # trades = pd.read_csv('trades.csv')

# # holdings.fillna(0, inplace=True)
# # trades.fillna(0, inplace=True)

# def preprocess_data(df):
#     df['text'] = df.apply(lambda row: ' '.join(row.astype(str)), axis=1)
#     return df['text'].tolist()

# texts = []
# for df in data_frames:
#     texts.extend(preprocess_data(df))

# model = SentenceTransformer('all-MiniLM-L6-v2')
# embeddings = model.encode(texts)

# # Step 5: Store in Chroma DB
# chroma = Chroma(Settings(
#     persist_directory="chroma_db_directory",
#     persist_period_seconds=60
# ))

# collection = chroma.create_collection(name="csv_embeddings")


# st.title('Property Data Chatbot')

# question = st.text_input("Hey, You can ask me anything about Proprty Deals made through PropertyLoop !!")


# if question:
#     if holdings is not None and question != "":
#         with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
#             tmp_file.write(uploaded_file.getvalue())
#             tmp_file_path = tmp_file.name

#         loader = CSVLoader(file_path=tmp_file_path, encoding="utf-8")
#         data = loader.load()

#         embeddings = OpenAIEmbeddings()
#         vector_store = DocArrayInMemorySearch.from_documents(data, embeddings)

#         qa = RetrievalQA.from_chain_type(
#             llm=OpenAI(),
#             chain_type="stuff",
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True,
#         )

#         result = qa({"query": question})

#         st.write(result["result"])
#     else:
#         st.error("Please upload a document and enter a query!")