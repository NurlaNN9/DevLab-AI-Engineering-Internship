# Product Review Sentiment Classifier

This project builds a sentiment classifier for real customer reviews and compares a classical machine-learning baseline with a pretrained transformer model.

The classifier assigns one of three labels to each review:

- Negative
- Neutral
- Positive

## Dataset

The project uses the [Yelp Review Full](https://huggingface.co/datasets/Yelp/yelp_review_full) dataset.

The original star ratings are converted into sentiment labels:

| Star rating | Sentiment |
|---|---|
| 1-2 | Negative |
| 3 | Neutral |
| 4-5 | Positive |

A balanced sample of 12,000 reviews is used:

- 9,000 training examples
- 3,000 test examples
- 3,000 examples per sentiment class in training
- 1,000 examples per sentiment class in testing

## Models

### Classical Baseline

- TF-IDF vectorization
- Unigrams and bigrams
- Logistic Regression
- Class weighting for imbalance handling

### Transformer Model

- Pretrained model: `cardiffnlp/twitter-roberta-base-sentiment-latest`
- Hugging Face Transformers
- Three-class sentiment classification
- The transformer is pretrained and is not fine-tuned in this project

## Evaluation

Both models are evaluated on the exact same train/test split.

The notebook includes:

- Accuracy
- Macro F1-score
- Weighted F1-score
- Per-class precision, recall and F1-score
- Confusion matrices
- Misclassified review analysis
- Confidence calibration check

## How to Run

Open the notebook in Google Colab and enable a GPU runtime:

```text
Runtime -> Change runtime type -> T4 GPU
```

Then run all cells from top to bottom.

To install dependencies locally:

```bash
pip install -r requirements.txt
```

## Project Structure

```text
Product-Review-Sentiment-Classifier/
├── documentation/
├── models/
├── Week06_Product_Review_Sentiment_Classifier.ipynb
├── README.md
├── REQUIRED-TASK.md
└── requirements.txt
```

## Deployment Recommendation

The transformer model is more suitable for offline weekly reporting, where stronger contextual understanding is more important than inference speed.

The TF-IDF + Logistic Regression model is more suitable for real-time support triage, where low latency, simplicity and low resource usage are more important.
