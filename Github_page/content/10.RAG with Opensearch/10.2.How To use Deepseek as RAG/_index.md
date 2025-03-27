---
title: "Use Deepseek as RAG?"
date :  "`r Sys.Date()`" 
weight: 2
chapter: false
pre: " <b> 10.2. </b> "
---

**_A Comprehensive Guide to Deploying RAG with DeepSeek Distill_**

Retrieval-Augmented Generation (RAG) is a powerful technique that combines information retrieval with text generation, enabling large language models (LLMs) like DeepSeek-R1 to provide accurate and up-to-date responses based on external knowledge sources. In this guide, we will implement RAG for the DeepSeek distill model with a detailed, professional, and engaging approach. Based on a DataCamp article, this guide covers every step, the purpose of each tool, and clear code annotations to make implementation easy and enjoyable.

---

## Understanding RAG and DeepSeek-R1

- **What is RAG (Retrieval-Augmented Generation)?**
  - RAG allows language models to fetch information from a knowledge base (e.g., PDF documents, text files) and integrate it into responses.
  - This method is great for answering questions based on data not included in the model's training set.

- **Meet DeepSeek-R1**
  - Developed by DeepSeek AI (China), DeepSeek-R1 excels in logical reasoning, mathematics, and real-time decision-making.
  - It also displays its reasoning process, enabling users to verify the logic behind responses.

In this guide, we'll build an RAG-powered chatbot with DeepSeek-R1 that runs locally and features a user-friendly web interface.

---

## What You'll Need

Here are the key tools and their roles:

1. **Ollama** – Runs large language models (like DeepSeek-R1) locally, ensuring privacy and fast processing.
2. **LangChain** – Helps integrate RAG by handling text processing, embedding generation, and vector database interactions.
3. **Chroma** – A vector database that stores and retrieves text embeddings efficiently.
4. **Gradio** – A Python library for building simple web interfaces for AI applications.
5. **PyMuPDF** – Extracts text from PDF files to create a knowledge base.
6. **RecursiveCharacterTextSplitter** – Splits long texts into smaller, manageable chunks.
7. **OllamaEmbeddings** – Converts text chunks into numerical embeddings for storage and retrieval.
8. **Chroma Client** – Manages storage and retrieval of embeddings within Chroma.

---

## Step-by-Step Deployment Guide

### Step 1: Set Up Your Environment

First, install Python (3.8 or later). Then, install the required libraries:

```bash
pip install ollama langchain gradio pymupdf chromadb
```

This command installs everything needed for our RAG chatbot.

---

### Step 2: Download the DeepSeek-R1 Model

To run DeepSeek-R1 locally, use Ollama to download the model:

```bash
ollama pull deepseek-r1:7b
```

- The `7b` refers to the 7-billion parameter version, balancing performance and system requirements.
- The model is stored locally and can run offline.

---

### Step 3: Load Your Knowledge Base

Let’s use a PDF document as our knowledge base. You can replace this with any text data.

```python
from langchain_community.document_loaders import PyMuPDFLoader

# Load a PDF file (replace with your actual path)
loader = PyMuPDFLoader("path/to/your/pdf.pdf")
documents = loader.load()
```

---

### Step 4: Split Text into Chunks

To make retrieval efficient, we split long texts into smaller segments:

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)
```

- Each chunk contains up to 1000 characters.
- A 200-character overlap maintains context across chunks.

---

### Step 5: Generate Embeddings

Convert text chunks into numerical embeddings:

```python
from langchain_community.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="deepseek-r1:7b")
```

---

### Step 6: Store Embeddings in Chroma

Save the embeddings into a vector database for retrieval:

```python
from langchain.vectorstores import Chroma

vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)
```

---

### Step 7: Build the RAG Retrieval & Response Function

Now, let’s create a function to retrieve relevant information and generate responses using DeepSeek-R1:

```python
import ollama

def ask_question(question):
    # Retrieve the top 3 most relevant chunks
    retrieved_chunks = vectorstore.similarity_search(question, k=3)
    context = " ".join([chunk.page_content for chunk in retrieved_chunks])

    # Create a prompt for DeepSeek-R1
    prompt = f"Based on the following information: {context}\n\nAnswer the question: {question}"

    # Generate a response
    response = ollama.chat(model="deepseek-r1:7b", messages=[{"role": "user", "content": prompt}])

    return response["message"]["content"]
```

---

### Step 8: Create a Web Interface with Gradio

A user-friendly chatbot interface with Gradio:

```python
import gradio as gr

def chatbot(question):
    return ask_question(question)

interface = gr.Interface(fn=chatbot, inputs="text", outputs="text", title="DeepSeek-R1 RAG Chatbot")
interface.launch()
```

---

## Running the Application

Save the script as `rag_chatbot.py` and run:

```bash
python rag_chatbot.py
```

A web interface will open, allowing users to ask questions and get RAG-powered responses.
