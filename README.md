# Property Data Chatbot Documentation

This repository contains scripts (`app.py` and `main.py`) for deploying a Property Data Chatbot using Streamlit, Groq API, and data from CSV files.

## `app.py`

### Overview

`app.py` is a script that implements a Property Data Chatbot using Streamlit for the user interface and Groq API for generating responses. It provides a simplified approach to interactively query data from static CSV files (`holdings.csv` and `trades.csv`).

### Features

- **Streamlit Integration**: Provides a user-friendly interface for users to input questions about property deals.
- **CSV Data Handling**: Loads data from `holdings.csv` and `trades.csv`, preprocesses it to handle missing values, and samples data for prompt generation.
- **Prompt Generation**: Generates prompts for the Groq API based on user questions and sampled data.
- **Response Generation**: Utilizes Groq API to generate responses based on the provided prompt and predefined chatbot guidelines.

### Usage

1. **Setup Environment**: Ensure Python environment is set up with necessary dependencies (`pandas`, `streamlit`, `groq`, `dotenv`).
2. **Configuration**: Set up environment variables (`GROQ_API_KEY`) in a `.env` file for Groq API authentication. Example `.env` file:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```
3. **Run Script**: Execute `app.py` and interact with the chatbot interface via a web browser.

### Example

```bash
streamlit run app.py
```

## `main.py`

### Overview

`main.py` implements a more advanced version of the Property Data Chatbot using additional libraries such as Sentence Transformers and Faiss for semantic search and retrieval of relevant data from multiple CSV files dynamically.

### Features

- **Dynamic CSV Loading**: Loads and processes multiple CSV files from a specified directory (`data`) using Pandas.
- **Text Embedding**: Utilizes Sentence Transformers to embed textual data for semantic similarity calculation.
- **Semantic Search**: Uses Faiss to perform efficient nearest neighbor search for retrieving relevant data based on user questions.
- **Prompt Generation**: Generates prompts based on the retrieved relevant data for querying Groq API.
- **Response Generation**: Uses Groq API to generate responses to user queries incorporating retrieved data.

### Usage

1. **Setup Environment**: Ensure Python environment is set up with necessary dependencies (`pandas`, `streamlit`, `groq`, `sentence-transformers`, `faiss`, `dotenv`).
2. **Configuration**: Set up environment variables (`GROQ_API_KEY`) in a `.env` file for Groq API authentication. Example `.env` file:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```
3. **Run Script**: Execute `main.py` and interact with the chatbot interface via a web browser.

### Example

```bash
streamlit run main.py
```

### Performance Consideration

- **Complexity**: `main.py` involves more computational overhead due to data preprocessing, embedding, and semantic search operations compared to `app.py`.
- **Speed**: `app.py` may perform faster as it directly samples and presents data without the additional complexity of semantic embedding and search.

### `.env` File

The `.env` file is used to securely store sensitive information such as API keys (`GROQ_API_KEY`). It allows the application to access these variables without hardcoding them in the source code, ensuring security and flexibility in different environments.

### `requirements.txt`

The `requirements.txt` file lists all Python dependencies required for running the scripts. You can install these dependencies using `pip`:

```bash
pip install -r requirements.txt
```

This ensures that all necessary libraries (`pandas`, `streamlit`, `groq`, `sentence-transformers`, `faiss`, `dotenv`) are installed in your Python environment before running `app.py` or `main.py`.

### Groq API

The Groq API is utilized in both scripts (`app.py` and `main.py`) for generating responses to user queries based on the provided data. It is chosen for its availability as a free API, allowing developers to integrate natural language processing capabilities into their applications without cost.

