# Week 04 — Retrieval-Augmented Generation (RAG)

This week focuses on building a Retrieval-Augmented Generation (RAG) system that answers questions using information retrieved from a document set.

## Required Task

### Document Q&A Assistant with RAG

The project uses the official NumPy User Guide as its knowledge base. The document is split into chunks, converted into embeddings, and indexed in FAISS for similarity-based retrieval.

The retrieved chunks are provided to a local LLM to generate grounded answers with source information.

The project also includes:

- Document chunking with overlap
- Sentence-Transformer embeddings
- Persistent FAISS vector storage
- Configurable top-k retrieval
- Grounded prompt construction
- Answers with source chunk and page information
- RAG vs. non-RAG comparison
- Out-of-scope question handling
- Retrieval evaluation with Hit Rate@3
- Retrieval ON/OFF grounding test

## Technologies

- Python
- Sentence-Transformers
- FAISS
- PyPDF
- Ollama
- Qwen2.5 1.5B
- Google Colab

## Results

- **Document:** NumPy User Guide
- **Chunks:** 2363
- **Chunk size:** 800 characters
- **Overlap:** 150 characters
- **Retrieval evaluation:** 100% Hit Rate@3
- **Out-of-scope tests:** 2/2 correctly declined
- **Retrieval gating test:** Answers changed when retrieval was disabled

## Structure

```text
Week-04/
└── Required-Tasks/
    └── Document-QA-Assistant-with-RAG/
        ├── models/
        │   ├── numpy_rag.index
        │   └── chunks.pkl
        └── Week04_Document_QA_RAG.ipynb
