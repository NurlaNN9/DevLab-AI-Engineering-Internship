# Document Q&A Assistant with RAG

Build a Retrieval-Augmented Generation system that answers questions about a specific document set by retrieving relevant chunks and grounding an LLM's answer in them. You must prove the assistant is genuinely using retrieval rather than answering from the model's own training knowledge - that grounding proof is the assessed skill, since most RAG demos skip verifying it.

## Learning objectives

- Chunk a document set using a documented, deliberate chunk size and overlap strategy
- Generate embeddings for each chunk using an embedding model
- Store and query embeddings in a vector store via similarity search
- Construct a prompt that injects only retrieved chunks, not the whole document, into the LLM context
- Demonstrate the difference between a grounded (RAG) answer and a non-grounded (parametric-only) answer for the same question
- Handle the 'not in the documents' case so the assistant admits it doesn't know rather than hallucinating
- Evaluate retrieval quality separately from generation quality using a small labeled question set

## Must-have features

- **Chunking Pipeline** — Documents split into chunks with a stated size/overlap, justified in the README.
- **Embedding & Vector Store** — All chunks embedded and indexed in FAISS or Chroma, with the index persisted to disk rather than rebuilt on every run.
- **Retrieval Function** — Top-k similarity search returning the most relevant chunks for a query, with k configurable.
- **Grounded Prompt Construction** — The LLM prompt explicitly separates 'context' (retrieved chunks) from 'question', visible in the code.
- **Grounding Proof** — A side-by-side table of at least 5 questions comparing the answer WITH retrieval vs. WITHOUT retrieval (LLM alone), showing where they genuinely differ.
- **Out-of-Scope Handling** — At least 2 test questions about topics NOT in the document set, where the assistant correctly declines instead of fabricating an answer.
- **Retrieval Evaluation** — A labeled set of 10 question -> expected-chunk pairs, with hit-rate (was the right chunk in the top-k?) reported.
- **Source Citation** — Every answer displays which chunk(s)/document section it was drawn from.
- **Anti-Cheat: Retrieval Must Actually Gate the Answer** — Disabling the vector store must measurably change answers on the grounding-proof questions. If answers are identical with retrieval on or off, the pipeline is not really using retrieval and will be rejected.

## Bonus features

- Add a re-ranking step after initial retrieval
- Support multiple document formats (PDF, Markdown, and web pages) in the same index
- Add conversation memory across multiple turns
- Expose the assistant through a simple chat UI (Streamlit or Gradio)

## Technical requirements

- **An embedding model** — OpenAI text-embedding-3-small, or a free local model via Sentence-Transformers - state which was chosen and why (cost vs. local trade-off).
- **FAISS or ChromaDB** — For the vector store.
- **An LLM for generation** — OpenAI API, or a local model via Ollama for a no-cost option - this connects directly to Week 7.
- **Python with LangChain or a from-scratch implementation** — Either is accepted, but building from scratch is encouraged so the mechanics aren't hidden behind a black box.

## RAG architecture overview

A plain-language overview of how retrieval-augmented generation systems are structured, from chunking to generation: [https://python.langchain.com/docs/concepts/rag/](https://python.langchain.com/docs/concepts/rag/)

## Mentor reference notes

The most common shortcut is skipping the grounding-proof comparison entirely. Graders should specifically confirm the WITH/WITHOUT retrieval answers are genuinely different, not copy-pasted placeholders.
