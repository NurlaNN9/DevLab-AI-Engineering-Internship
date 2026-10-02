# Week 04 — Required Tasks

This folder contains the required task completed for Week 04 of the AI Engineering Internship.

## Required Task

### Document Q&A Assistant with RAG

The goal of this task is to build a Retrieval-Augmented Generation (RAG) system that answers questions using information retrieved from a specific document set.

The implementation uses the official NumPy User Guide as the knowledge base and includes:

- Document text extraction and chunking
- Sentence-Transformer embeddings
- FAISS vector storage
- Persistent vector index
- Top-k similarity retrieval
- Grounded prompt construction
- Local LLM generation with Ollama
- Source chunk and page information
- RAG vs. non-RAG comparison
- Out-of-scope question handling
- Retrieval evaluation
- Retrieval ON/OFF grounding test

## Implementation

The complete implementation is available in:

`Document-QA-Assistant-with-RAG/`

The project folder contains the Jupyter notebook and the persisted FAISS vector store files.

## Results

The retrieval system achieved **100% Hit Rate@3** on the 10-question labeled retrieval evaluation set.

The assistant also correctly declined both out-of-scope test questions, and disabling retrieval changed the answers in the grounding test, demonstrating that retrieval genuinely affects the generated responses.
