# AI Assistant – Retrieval-Augmented Generation (RAG) System

An intelligent assistant built using LangChain, ChromaVectorStore (vector store) and Google Generative AI-models.  
It lets you ingest documents / web content, embed and store them with metadata, then answer user queries by retrieving relevant chunks and generating responses.

---

## Features

- Load and **chunk** documents/web content from URLs or files.
- Generate embeddings and store them in Chroma with metadata (URL, page, etc).
- Perform **semantic search** (with query embedding) and metadata filtering.
- Use a Google Generative AI model to **answer questions** based on retrieved context.
- Simple chat interface (CLI) with “type ‘exit’ to quit” support.

---

## Getting Started

### Prerequisites

- Python 3.10 or newer
- API key for Google Generative AI
- `pip install` ability

### Installation

```bash
git clone https://github.com/your-username/ai_assistant_rag.git
cd ai_assistant_rag
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
