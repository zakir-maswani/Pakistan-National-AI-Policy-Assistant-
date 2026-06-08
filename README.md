<div align="center">

# 🇵🇰 Pakistan National AI Policy Assistant

**An intelligent RAG-powered chatbot for exploring Pakistan's National AI Policy 2025**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![LangChain](https://img.shields.io/badge/LangChain-0.2%2B-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com)
[![Groq](https://img.shields.io/badge/Groq-LLaMA%203.1-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20Store-0467DF?style=for-the-badge&logo=meta&logoColor=white)](https://faiss.ai)
[![License: MIT](https://img.shields.io/badge/License-Apache-yellow.svg?style=for-the-badge)](LICENSE)

<br/>

> Ask natural language questions about Pakistan's National AI Policy 2025 and get accurate, context-aware answers — powered by Retrieval-Augmented Generation (RAG).

<br/>

</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [📁 Project Structure](#-project-structure)
- [⚙️ Prerequisites](#️-prerequisites)
- [🚀 Getting Started](#-getting-started)
- [🔑 Environment Variables](#-environment-variables)
- [🖥️ Usage](#️-usage)
- [🔌 API Reference](#-api-reference)
- [🛣️ Roadmap](#️-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Features

- 🤖 **RAG Pipeline** — Retrieval-Augmented Generation over the official policy PDF
- ⚡ **Groq LLaMA 3.1** — Ultra-fast inference via `llama-3.1-8b-instant`
- 🔍 **Semantic Search** — HuggingFace `all-MiniLM-L6-v2` embeddings + FAISS vector store
- 💬 **Chat Interface** — Clean, dark-themed UI with sidebar history and suggestion chips
- 🔧 **FastAPI Backend** — Async REST API with auto-generated `/docs`
- 📐 **Resizable Sidebar** — Drag-to-resize panel for conversation history
- 🌐 **CORS Ready** — Configured for local dev and easy deployment

---

## 🏗️ Architecture

```
User Query
    │
    ▼
┌─────────────────┐     HTTP POST /ask/     ┌──────────────────────────┐
│  Frontend (HTML) │ ──────────────────────► │  FastAPI Backend         │
│  original_index  │                         │  main.py                 │
└─────────────────┘ ◄────────────────────── └──────────┬───────────────┘
        ▲                  JSON Response                │
        │                                               ▼
        │                                   ┌──────────────────────────┐
        │                                   │  RAG Chain (utils.py)        │
        │                                   │                              │
        │                                   │  1. PyPDFLoader              │
        │                                   │     └─ Load PDF              │
        │                                   │  2. RecursiveTextSplitter.   │
        │                                   │     └─ Chunk (1000/200)      │
        │                                   │  3. HuggingFace Embeds       │
        │                                   │     └─ all-MiniLM-L6-v2      │
        │                                   │  4. FAISS VectorStore        │
        │                                   │     └─ Top-k=3 Retrieval     │
        │                                   │  5. ChatGroq (LLaMA 3.1)     │
        └───────────────────────────────────│     └─ Generate Answer   │
                                            └──────────────────────────┘
```

---

## 📁 Project Structure

```
national-ai-policy-assistant/
│
├── Backend/
│   ├── main.py               # FastAPI app, lifespan, CORS, routes
│   ├── utils.py              # RAG chain: PDF load → embed → retrieve → generate
│   └── NationalAIPolicy.pdf  # 📄 Policy document (add manually — not tracked by git)
│
├── Frontend/
│   └── index.html            # Single-page chat UI
│
├── .env                      # 🔒 Secret keys (never commit — in .gitignore)
├── .env.example              # ✅ Safe template to share
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Prerequisites

| Requirement | Version |
|---|---|
| Python | 3.10 or higher |
| pip | Latest |
| Groq API Key | [Get one free →](https://console.groq.com) |
| National AI Policy PDF | Obtain from official source |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/national-ai-policy-assistant.git
cd national-ai-policy-assistant
```

### 2. Create & Activate a Virtual Environment

```bash
# Create
python -m venv venv

# Activate — macOS/Linux
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
cp .env.example .env
```

Open `.env` and fill in your credentials (see [Environment Variables](#-environment-variables)).

### 5. Add the Policy PDF

Place the `NationalAIPolicy.pdf` file inside the `Backend/` folder:

```
Backend/
└── NationalAIPolicy.pdf   ← add here
```

> ⚠️ The PDF is excluded from version control via `.gitignore`. You must add it manually.

### 6. Run the Backend

```bash
cd Backend
python main.py
```

The API will be live at: **`http://127.0.0.1:8000`**  
Interactive API docs: **`http://127.0.0.1:8000/docs`**

### 7. Open the Frontend

Open `Frontend/index.html` directly in your browser, **or** let FastAPI serve it:

```
http://127.0.0.1:8000/
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root (or `Backend/`) with the following:

```env
# .env.example — copy to .env and fill in your values

# Groq API Key (required)
# Get yours at: https://console.groq.com
GROQ_API_KEY=your_groq_api_key_here
```

> 🔒 **Never commit your `.env` file.** It is already listed in `.gitignore`.

---

## 🖥️ Usage

1. **Start the server** and open the app in your browser.
2. Use the **suggestion chips** (Policy Goals, Summarize AI Policy, Infrastructure) for quick queries.
3. Type any question about Pakistan's National AI Policy in the input box and press **Send** or hit `Enter`.
4. Your **conversation history** is tracked in the sidebar for the session.
5. Click **New Chat** to start a fresh session.

### Example Questions

```
📌 What are the main goals of Pakistan's National AI Policy?
📌 How does the policy address data privacy?
📌 What sectors are prioritized for AI adoption?
📌 Summarize the digital infrastructure strategy.
📌 What role does the government play in AI governance?
```

---

## 🔌 API Reference

### `POST /ask/`

Ask a question about the policy document.

**Query Parameter**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `question` | `string` | ✅ Yes | The question to ask the RAG chain |

**Request Example**

```bash
curl -X POST "http://127.0.0.1:8000/ask/?question=What%20are%20the%20AI%20policy%20goals"
```

**Response Example**

```json
{
  "answer": "The National AI Policy 2026 outlines five key goals including..."
}
```

**Error Response**

```json
{
  "detail": "RAG not initialized"
}
```

---

### `GET /`

Serves the frontend `index.html`.

---

## 🛣️ Roadmap

- [x] RAG pipeline with FAISS + HuggingFace embeddings
- [x] Groq LLaMA 3.1 integration
- [x] FastAPI backend with CORS
- [x] Chat UI with history sidebar
- [ ] 🔄 Persistent chat history (localStorage / DB)
- [ ] 📚 Source citation with page numbers
- [ ] 🌙 Light / Dark mode toggle
- [ ] 🐳 Docker deployment
- [ ] ☁️ Deployment guide (Railway / Render / HuggingFace Spaces)
- [ ] 🌍 Urdu language support

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature-name`
3. **Commit** your changes: `git commit -m 'Add: brief description'`
4. **Push** to the branch: `git push origin feature/your-feature-name`
5. **Open** a Pull Request

Please make sure your code is clean and tested before submitting.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Built with ❤️ for Pakistan 🇵🇰

*Powered by [LangChain](https://langchain.com) · [Groq](https://groq.com) · [FastAPI](https://fastapi.tiangolo.com) · [FAISS](https://faiss.ai)*

</div>
