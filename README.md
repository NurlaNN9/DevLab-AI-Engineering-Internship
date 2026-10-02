# DevLab AI Engineering Internship

This repository contains my projects, workflows, assignments, experiments, and technical documentation completed during the **DevLab AI Engineering Internship**.

The repository documents my progress through the internship and focuses on practical AI engineering, automation, APIs, machine learning, deep learning, computer vision, retrieval-augmented generation, and AI-powered applications.

## Repository Structure

```text
DevLab-AI-Engineering-Internship/
│
├── Week-01/
│   ├── Required-Tasks/
│   │   └── Customer-Support-Ticket-Bot/
│   ├── Bonus-Tasks/
│   │   ├── Daily-Personal-Digest-Bot/
│   │   └── FAQ-Bot/
│   └── README.md
│
├── Week-02/
│   ├── Required-Tasks/
│   │   └── Handwritten-Digit-Classifier/
│   │       ├── documentation/
│   │       ├── handwritten-digits/
│   │       ├── models/
│   │       ├── Week02_MNIST_CNN_vs_MLP.ipynb
│   │       └── README.md
│   └── README.md
│
├── Week-03/
│   ├── Required-Tasks/
│   │   └── License-Plate-Detection-and-Recognition-Pipeline/
│   │       ├── documentation/
│   │       ├── models/
│   │       ├── Week03_License_Plate_Detection_OCR.ipynb
│   │       └── README.md
│   └── README.md
│
├── Week-04/
│   ├── Required-Tasks/
│   │   ├── Document-QA-Assistant-with-RAG/
│   │   │   ├── models/
│   │   │   │   ├── numpy_rag.index
│   │   │   │   └── chunks.pkl
│   │   │   └── Week04_Document_QA_RAG.ipynb
│   │   ├── REQUIRED-TASK.md
│   │   └── README.md
│   └── README.md
│
└── README.md
```

Each week contains its own documentation, implementation files, experiments, testing evidence, and supporting resources.

---

## Week 01 — AI Automation with n8n

Week 01 focuses on building practical automation workflows with **n8n**, external APIs, Telegram, Google Sheets, and AI models.

### Required Task

**Customer Support Ticket Bot**

An AI-powered customer support workflow that:

- Receives support requests through Telegram
- Uses a locally hosted **Gemma 4** model through **Ollama**
- Classifies requests into Billing, Technical, and General categories
- Routes requests dynamically
- Logs tickets to Google Sheets
- Integrates an external API
- Handles invalid input and service failures
- Sends admin alerts for Technical tickets

Project directory:

`Week-01/Required-Tasks/Customer-Support-Ticket-Bot/`

### Optional Task 01

**Daily Personal Digest Bot**

An automated daily Telegram digest that combines:

- Weather information
- BBC World news
- Google Sheets to-do items
- Motivational quotes
- Dynamic weather visuals
- Scheduled and `/digest` execution

Project directory:

`Week-01/Bonus-Tasks/Daily-Personal-Digest-Bot/`

### Optional Task 02

**FAQ Bot Backed by a Knowledge-Base Spreadsheet**

A spreadsheet-backed FAQ retrieval bot featuring:

- Google Sheets knowledge base
- Generic Levenshtein similarity matching
- Similarity threshold and safe fallback
- Unanswered-question logging
- Live `/addfaq` administration
- Typo-tolerant matching
- `/yes` and `/no` follow-up confirmation

Project directory:

`Week-01/Bonus-Tasks/FAQ-Bot/`

---

## Week 02 — Computer Vision with PyTorch

Week 02 focuses on deep learning and image classification using **PyTorch** and the **MNIST handwritten digit dataset**.

The main objective was to build a convolutional neural network from scratch, compare it with a fully connected neural network, and test its performance on handwritten digits outside the MNIST dataset.

### Required Task

**Handwritten Digit Classifier with a CNN (MNIST)**

A computer vision project that:

- Loads and normalizes the MNIST dataset
- Creates separate training, validation, and test datasets
- Builds a CNN with two convolution and pooling blocks
- Trains an MLP baseline under the same conditions
- Tracks training and validation loss and accuracy
- Compares CNN and MLP performance
- Generates and interprets a confusion matrix
- Tests the CNN on five custom handwritten digit images
- Improves custom image preprocessing
- Saves and reloads trained model weights for inference

#### Model Performance

| Model | Validation Accuracy | Test Accuracy |
|---|---:|---:|
| CNN | 98.58% | 98.82% |
| MLP | 96.68% | 97.31% |
| CNN + Augmentation | 98.82% | 99.01% |

The CNN achieved higher test accuracy than the MLP under the same training conditions.

#### Custom Handwriting Experiment

The original CNN was also tested on five handwritten digit images created outside the MNIST dataset.

| Preprocessing Method | Correct Predictions | Accuracy |
|---|---:|---:|
| Original preprocessing | 2/5 | 40% |
| Improved preprocessing | 5/5 | 100% |

Improved preprocessing included cropping the empty background, resizing the digit while preserving its aspect ratio, and centering it on a 28×28 canvas.

The model was not retrained for this experiment. The five-image result demonstrates the effect of preprocessing on this small custom sample, rather than general accuracy on real-world handwriting.

#### Bonus Experiments

Two bonus experiments were completed:

- **Data Augmentation:** Applied small rotations and shifts during training. The augmented CNN achieved 99.01% test accuracy.
- **Filter Visualization:** Visualized the learned filters of the CNN's first convolutional layer.

Project directory:

`Week-02/Required-Tasks/Handwritten-Digit-Classifier/`

---

## Week 03 — License Plate Detection and Recognition

Week 03 focuses on building an end-to-end computer vision pipeline that combines **object detection** and **optical character recognition (OCR)**.

### Required Task

**License Plate Detection and Recognition Pipeline**

The project combines **YOLOv8** and **EasyOCR** to detect license plates and recognize the text inside them.

The pipeline:

- Uses a labeled license plate dataset from Roboflow
- Trains a YOLOv8n object detection model
- Detects license plates in vehicle images
- Crops detected plate regions
- Applies OCR to the detected plates using EasyOCR
- Cleans recognized plate text
- Supports images containing multiple vehicles
- Evaluates detection using IoU and YOLO validation metrics
- Evaluates OCR using exact-match accuracy and Character Error Rate (CER)
- Includes failure-case analysis

#### Detection Performance

| Metric | Result |
|---|---:|
| Precision | 93.7% |
| Recall | 88.1% |
| mAP@50 | 92.2% |
| mAP@50-95 | 68.7% |
| Mean Test IoU | 74.78% |

#### OCR Evaluation

OCR was evaluated using 22 manually transcribed test images.

| Metric | Result |
|---|---:|
| Exact-Match Accuracy | 22.73% |
| Mean CER | 0.7718 |

The results demonstrate the difference between strong license plate localization and the more difficult task of accurately recognizing plate text under varying image conditions.

Project directory:

`Week-03/Required-Tasks/License-Plate-Detection-and-Recognition-Pipeline/`

---

## Week 04 — Retrieval-Augmented Generation

Week 04 focuses on building a **Retrieval-Augmented Generation (RAG)** system that answers questions using information retrieved from a specific document set.

The main objective is not only to build a working RAG pipeline, but also to verify that retrieval genuinely affects the generated answers.

### Required Task

**Document Q&A Assistant with RAG**

The project uses the official **NumPy User Guide** as its document knowledge base.

The system:

- Extracts text from the source PDF
- Splits the document into overlapping chunks
- Generates local embeddings using Sentence-Transformers
- Stores embeddings in a persistent FAISS vector index
- Performs configurable top-k similarity search
- Supplies only retrieved chunks to the LLM
- Separates retrieved context from the user question in the prompt
- Generates grounded answers using a local model through Ollama
- Displays source chunk and page information
- Handles questions outside the document set
- Compares answers with and without retrieval
- Evaluates retrieval separately from generation
- Tests whether disabling retrieval changes the generated answers

#### RAG Configuration

| Component | Configuration |
|---|---|
| Knowledge Base | NumPy User Guide |
| Chunk Size | 800 characters |
| Chunk Overlap | 150 characters |
| Total Chunks | 2363 |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Store | FAISS |
| Generation Model | Qwen2.5 1.5B via Ollama |
| Retrieval | Top-k similarity search |

#### Retrieval Evaluation

A labeled set of 10 question-to-expected-chunk pairs was used to evaluate retrieval independently from answer generation.

| Metric | Result |
|---|---:|
| Hit Rate@3 | 100% |
| Out-of-Scope Tests Correctly Declined | 2/2 |
| Retrieval Gating Test | Answers changed when retrieval was disabled |

The FAISS index and chunk metadata are persisted to disk so that the vector store can be loaded without rebuilding it on every run.

Project directory:

`Week-04/Required-Tasks/Document-QA-Assistant-with-RAG/`

---

## Technologies & Tools

Technologies used throughout the internship currently include:

### AI & Machine Learning

- **PyTorch** — deep learning model development and training
- **Torchvision** — MNIST dataset loading and image transformations
- **CNN** — convolutional neural network for image classification
- **MLP** — fully connected neural network baseline
- **YOLOv8** — license plate object detection
- **EasyOCR** — optical character recognition
- **Sentence-Transformers** — local text embedding generation
- **all-MiniLM-L6-v2** — embedding model used for document retrieval
- **FAISS** — vector storage and similarity search
- **Qwen2.5 1.5B** — local language model used for grounded answer generation
- **scikit-learn** — model evaluation and classification metrics
- **NumPy** — numerical operations
- **Pandas** — experiment results and comparison tables
- **Matplotlib** — training curves and visualizations
- **Pillow** — image preprocessing
- **OpenCV** — computer vision and image processing
- **PyPDF** — PDF text extraction
- **Google Colab** — notebook execution and model training

### Automation & Integration

- **n8n** — workflow automation
- **JavaScript** — workflow logic and data processing
- **Docker** — local service deployment
- **Ollama** — local AI model execution
- **Gemma 4** — local language model used in Week 01
- **Telegram Bot API** — user interaction
- **Google Sheets API** — data storage and knowledge-base integration
- **REST APIs** — external data integration
- **Open-Meteo API** — weather data
- **BBC RSS** — news data
- **ZenQuotes** — motivational quote data
- **Levenshtein Distance** — fuzzy text similarity

---

## Repository Goals

This repository is intended to:

- Document my progress during the internship
- Build practical AI engineering experience
- Apply AI models to real automation workflows
- Practice API and third-party service integration
- Develop reliable workflow error handling
- Build and evaluate machine learning and deep learning models
- Develop practical computer vision pipelines
- Combine object detection with OCR
- Explore vector embeddings and similarity search
- Build Retrieval-Augmented Generation systems
- Evaluate retrieval separately from generation
- Understand and test LLM grounding
- Handle out-of-scope questions without hallucination
- Maintain reproducible project documentation
- Track the development of increasingly advanced AI systems

---

## Current Progress

| Week | Focus | Status |
|---|---|---|
| Week 01 | AI Automation with n8n | ✅ Completed |
| Week 02 | Computer Vision with PyTorch | ✅ Completed |
| Week 03 | Object Detection & OCR | ✅ Completed |
| Week 04 | Retrieval-Augmented Generation | ✅ Completed |

Additional weeks and projects will be added as the internship progresses.

---

## About

This repository was created as part of the **DevLab AI Engineering Internship** and serves as a technical portfolio of the work completed throughout the program.

Each project directory contains its own implementation files, supporting resources, evaluation results, and documentation.
