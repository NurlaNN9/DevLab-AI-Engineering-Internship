# Week 6 — Product Review Sentiment Classification

This week focuses on sentiment classification for real customer reviews: building a classical machine-learning baseline, applying a pretrained transformer model, and comparing both approaches on identical data splits.

## Required Task

### Product Review Sentiment Classifier

The required project is a sentiment classifier that assigns real product and service reviews to one of three sentiment classes: negative, neutral, or positive.

The project uses the Yelp Review Full dataset and compares a TF-IDF + Logistic Regression baseline with a pretrained transformer model. Both models are evaluated on the same train/test split, with per-class precision, recall, and F1-score reported for each model.

The project includes:

- A real-world review dataset with more than 1,000 labeled examples.
- Text preprocessing and stratified balanced sampling.
- A TF-IDF + Logistic Regression classical baseline.
- A pretrained Hugging Face transformer for three-class sentiment classification.
- Identical train/test splits for both models.
- Per-class precision, recall, and F1-score evaluation.
- Class imbalance measurement and class-weighting mitigation.
- Confusion matrices and model comparison metrics.
- Error analysis of misclassified reviews.
- A confidence calibration check.
- A deployment recommendation based on accuracy, latency, and resource trade-offs.

## Technologies

- Python
- pandas
- NumPy
- scikit-learn
- Hugging Face Transformers
- Hugging Face Datasets
- PyTorch
- Matplotlib
- Google Colab

## Dataset

The project uses the [Yelp Review Full](https://huggingface.co/datasets/Yelp/yelp_review_full) dataset.

The original star ratings are converted into sentiment labels:

| Star rating | Sentiment |
|---|---|
| 1–2 | Negative |
| 3 | Neutral |
| 4–5 | Positive |

A balanced sample of 12,000 reviews is used:

| Split | Negative | Neutral | Positive | Total |
|---|---:|---:|---:|---:|
| Train | 3,000 | 3,000 | 3,000 | 9,000 |
| Test | 1,000 | 1,000 | 1,000 | 3,000 |

## Models

### Classical Baseline

- TF-IDF vectorization
- Unigrams and bigrams
- Logistic Regression
- `class_weight="balanced"` for imbalance handling

### Transformer Model

- Pretrained model: `cardiffnlp/twitter-roberta-base-sentiment-latest`
- Hugging Face Transformers
- Three-class sentiment classification
- The transformer is pretrained and is not fine-tuned in this project

## Results

The notebook reports the following metrics on the held-out test split:

| Model | Accuracy | Macro F1 | Weighted F1 |
|---|---:|---:|---:|
| TF-IDF + Logistic Regression | To be filled after running the notebook | To be filled after running the notebook | To be filled after running the notebook |
| Pretrained Transformer | To be filled after running the notebook | To be filled after running the notebook | To be filled after running the notebook |

The notebook also includes per-class precision, recall, and F1-score, confusion matrices, misclassified review analysis, and a confidence calibration check.

## Deployment Recommendation

The transformer model is more suitable for offline weekly reporting, where stronger contextual understanding is more important than inference speed.

The TF-IDF + Logistic Regression model is more suitable for real-time support triage, where low latency, simplicity, and low resource usage are more important.

## Bonus Features

The project also includes the following bonus components:

- A neutral sentiment class.
- A confidence calibration check.
- A live-testing function for individual reviews.

## Project Structure

```text
Week-06/
├── README.md
└── Required-Tasks/
    └── Product-Review-Sentiment-Classifier/
        ├── documentation/
        │   └── README.md
        ├── Week06_Product_Review_Sentiment_Classifier.ipynb
        ├── README.md
        ├── REQUIRED-TASK.md
        ├── requirements.txt
        └── .gitignore
```

The dataset is downloaded directly from Hugging Face when the notebook is run. Dataset files and transformer model weights are not included in the repository because of their size.

## Run the Notebook

Open the notebook in Google Colab and enable a GPU runtime:

```text
Runtime -> Change runtime type -> T4 GPU
```

Then run all cells from top to bottom.

To install dependencies locally:

```bash
pip install -r requirements.txt
```

## Task Specification

The complete task specification is available at:

```text
Required-Tasks/Product-Review-Sentiment-Classifier/REQUIRED-TASK.md
```
