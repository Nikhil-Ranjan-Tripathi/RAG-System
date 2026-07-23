# 📚 RAG Document Q&A System

A powerful Retrieval-Augmented Generation (RAG) system that enables intelligent question-answering over your documents using LangChain, ChromaDB, and OpenAI/Hugging Face embeddings.

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://python.org)
[![LangChain](https://img.shields.io/badge/langchain-0.3.27-green.svg)](https://langchain.com)

---

## 🌟 Features

- 📄 **Multi-format Document Support**: Load and process Markdown, PDF, TXT, and more
- ✂️ **Intelligent Text Chunking**: Smart document splitting with overlap for better context
- 🧠 **Dual Embedding Options**:
  - OpenAI embeddings (paid)
  - Hugging Face embeddings (free)
- 🗄️ **Vector Database**: ChromaDB for efficient similarity search
- 🔍 **Semantic Search**: Find relevant information using embeddings
- 💬 **Question Answering**: Ask questions and get answers from your documents
- 🔐 **Secure API Key Management**: Uses `.env` for environment variables

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Conda (recommended) or pip
- OpenAI API key (optional for free embeddings)

##📁 Project Structure

rag-document-qa/
├── 📂 data/                    # Document storage
│   ├── 📄 alice.md
│   └── 📄 sample.md
├── 📂 data/chroma/             # Vector database (auto-generated)
├── 📄 create_database.py       # Main script
├── 📄 query_data.py            # Query interface
├── 📄 requirements.txt         # Dependencies
├── 📄 .env                     # Environment variables
└── 📄 README.md                # Documentation

##📦 Dependencies

langchain==0.3.27
langchain-community==0.3.27
langchain-core==0.3.72
chromadb
sentence-transformers
pypdf
python-dotenv
tiktoken
openai

##🎯 Use Cases
- 📝 Document Summarization: Extract key information from reports
- 📚 Research Assistance: Query academic papers
- 🏢 Corporate Knowledge Base: Search internal documentation
- 📖 Personal Knowledge Management: Organize and retrieve notes
- 🎓 Educational Support: Create study assistants

