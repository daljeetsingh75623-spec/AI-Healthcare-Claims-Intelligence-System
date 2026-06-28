# 🏥 AI Healthcare Claims Intelligence System

An enterprise-grade AI-powered Healthcare Claims Intelligence System built using **FastAPI, NVIDIA Llama, LangChain, FAISS, and Retrieval-Augmented Generation (RAG)**.

The system enables healthcare providers and insurance companies to upload medical claim documents, index them into a vector database, and ask natural language questions grounded in the uploaded documents.

---

# 🚀 Features

### ✅ AI Chat Assistant

* NVIDIA Llama 3.3 Integration
* REST API with FastAPI
* Context-aware responses

### ✅ Document Intelligence

* Upload Healthcare Claim PDFs
* Upload Insurance Policy PDFs
* Automatic PDF Text Extraction
* Document Validation

### ✅ Retrieval-Augmented Generation (RAG)

* Recursive Text Chunking
* HuggingFace Embeddings
* FAISS Vector Database
* Semantic Search
* Context-Aware Question Answering

### ✅ REST APIs

| Endpoint                 | Description                           |
| ------------------------ | ------------------------------------- |
| `GET /`                  | Application Status                    |
| `GET /health`            | Health Check                          |
| `POST /chat`             | AI Chat                               |
| `POST /documents/upload` | Upload & Index PDF                    |
| `POST /rag/ask`          | Ask Questions from Uploaded Documents |

---

# 🏗️ System Architecture

```text
                        PDF Upload
                             │
                             ▼
                     PyMuPDF Extraction
                             │
                             ▼
                    Recursive Chunking
                             │
                             ▼
                 HuggingFace Embeddings
                             │
                             ▼
                      FAISS Vector DB
                             │
                             ▼
                   Semantic Retrieval
                             │
                             ▼
                    NVIDIA Llama 3.3
                             │
                             ▼
                      AI Generated Answer
```

---

# 📂 Project Structure

```text
AI-Healthcare-Claims-Intelligence-System
│
├── app
│   ├── agents
│   ├── api
│   ├── core
│   ├── database
│   ├── llm
│   ├── models
│   ├── prompts
│   ├── rag
│   ├── services
│   ├── utils
│   └── main.py
│
├── data
├── docs
├── uploads
├── vector_db
├── requirements.txt
├── run.py
└── README.md
```

---

# 🛠️ Technology Stack

### Backend

* Python
* FastAPI
* Uvicorn

### AI & LLM

* NVIDIA Llama 3.3
* LangChain
* HuggingFace Embeddings

### Vector Database

* FAISS

### PDF Processing

* PyMuPDF

### Data Validation

* Pydantic

### API Documentation

* Swagger UI
* OpenAPI

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Healthcare-Claims-Intelligence-System.git

cd AI-Healthcare-Claims-Intelligence-System
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
NVIDIA_API_KEY=YOUR_NVIDIA_API_KEY

BASE_URL=https://integrate.api.nvidia.com/v1

MODEL_NAME=meta/llama-3.3-70b-instruct
```

---

# ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# 💡 Example Workflow

### Upload a Policy Document

```
POST /documents/upload
```

↓

Document is:

* Uploaded
* Extracted
* Chunked
* Embedded
* Indexed into FAISS

---

### Ask Questions

```
POST /rag/ask
```

Example:

```json
{
  "question":"What does this insurance policy cover?"
}
```

Example Response:

```json
{
    "answer":"The policy covers nursing charges, laboratory investigations, radiology, physiotherapy, and hospital overheads."
}
```

---

# 📈 Current Progress

## ✅ Completed

* FastAPI Backend
* NVIDIA LLM Integration
* REST APIs
* PDF Upload
* PDF Text Extraction
* RAG Pipeline
* HuggingFace Embeddings
* FAISS Vector Database
* Semantic Search
* Healthcare Document Question Answering

---

## 🚧 Upcoming Features

* Multi-Document Support
* Medical Claim Summarization
* Insurance Coverage Verification
* Fraud Detection Agent
* Missing Document Detection
* Claim Approval Recommendation
* Multi-Agent AI Workflow (LangGraph)
* PostgreSQL Integration
* Redis Caching
* Airflow ETL Pipelines
* React Dashboard
* Docker Deployment
* CI/CD with GitHub Actions

---

# 🎯 Future Roadmap

* Enterprise Authentication
* OCR for Scanned PDFs
* Snowflake Integration
* Pinecone Support
* Multi-Tenant Architecture
* Explainable AI (XAI)
* Real-Time Claim Analytics
* Healthcare KPI Dashboard

---

# 👨‍💻 Author

**Daljeet Singh**

AI Engineer | Python | FastAPI | Generative AI | LangChain | RAG | NVIDIA LLM | FAISS
