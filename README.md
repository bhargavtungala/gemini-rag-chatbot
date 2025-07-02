# 🤖 Gemini RAG Chatbot

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-0.4.24-A6A6FA?style=for-the-badge&logo=chroma&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.2.1-FFC107?style=for-the-badge&logo=langchain&logoColor=black)
![Vertex AI](https://img.shields.io/badge/Google_Cloud-Vertex_AI-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-orange?style=for-the-badge&logo=html5&logoColor=white)

A simple yet powerful Retrieval Augmented Generation (RAG) chatbot built with **FastAPI**, **ChromaDB**, and **Gemini** via **Vertex AI**. Upload your own PDF or TXT documents, and chat with a bot that leverages that content for accurate, context-aware responses.

---

## ✨ Features

- 📄 **Document Upload**: Ingest `.pdf` and `.txt` documents via UI.
- 🧠 **RAG Pipeline**: Combines document retrieval + Gemini for enhanced QA.
- 📦 **ChromaDB**: Vector store for fast semantic search.
- 🧬 **Google Vertex AI**: Uses Gemini for chat and optionally Gecko for embeddings.
- 🌐 **FastAPI + HTML Frontend**: Clean, simple web interface.
- 🔄 **Hot Reloading**: Dev-friendly setup with `--reload`.

---

## ⚙️ Prerequisites

- Python 3.9+
- Google Cloud project with:
  - Vertex AI API enabled
  - Authentication set up via:
    ```bash
    gcloud auth application-default login
    ```
- OpenAI key (optional, if switching from Vertex AI embeddings)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/bhargavtungala/gemini-rag-chatbot.git
cd gemini-rag-chatbot
