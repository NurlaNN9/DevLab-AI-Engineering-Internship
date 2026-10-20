# Product Review Sentiment Classifier

Build a sentiment classifier for real product and service reviews that predicts positive, negative, or neutral sentiment. Compare a classical machine learning baseline against a pretrained or fine-tuned transformer to demonstrate the trade-off between simplicity and performance.

The main assessment criterion is a genuine comparison using identical data splits, not accuracy alone.

## Learning Objectives

- Clean and preprocess raw review text appropriately for the chosen method.
- Build a classical ML baseline using TF-IDF and Logistic Regression or SVM, trained on labeled review data.
- Use a pretrained or fine-tuned transformer for the same classification task.
- Evaluate both models using precision, recall, and F1-score for each class, not just overall accuracy, since review sentiment is often imbalanced.
- Analyze misclassified examples to identify systematic weaknesses, such as sarcasm, negation, or mixed sentiment.
- Justify which model to deploy based on accuracy, latency, and resource trade-offs.

## Must-Have Features

- **Real Dataset:** Use a real-world review dataset, such as Amazon, Yelp, IMDb, or a small self-scraped dataset with permission, containing at least 1,000 labeled examples.
- **Classical Baseline:** Train and evaluate a TF-IDF-based classical classifier.
- **Transformer Model:** Train or evaluate a pretrained/fine-tuned transformer using the identical train/test split as the baseline.
- **Per-Class Metrics:** Report precision, recall, and F1-score for every sentiment class for both models, not just overall accuracy.
- **Class Imbalance Handling:** Measure the dataset's class distribution and apply at least one mitigation strategy: class weighting, resampling, or an explicit, reasoned decision to leave the imbalance unaddressed.
- **Error Analysis:** Review at least five misclassified examples and provide a written hypothesis explaining why the model misclassified each one.
- **Model Comparison Verdict:** Recommend which model to deploy for a specific hypothetical use case, such as real-time support triage or offline weekly reporting.
- **Identical Data Splits:** Train and evaluate both models on exactly the same train/test split, using the same random seed or a saved split file. Mismatched splits invalidate the comparison and will be rejected.

## Bonus Features

- Add a neutral class if the dataset supports it, and investigate whether including it affects binary classification performance.
- Test both models on out-of-domain text, such as training on product reviews and testing on restaurant reviews, to evaluate generalization.
- Implement a simple confidence-calibration check to determine whether high-confidence predictions are more likely to be correct.
- Wrap the better-performing model in a small CLI or API for live testing.

## Technical Requirements

- **scikit-learn:** Required for the classical baseline.
- **Hugging Face Transformers:** Use a free pretrained model, such as a DistilBERT sentiment model, or fine-tune your own model. Clearly state which approach and model were used.
- **Sufficient Compute:** Google Colab's free-tier GPU is sufficient for the transformer. Full fine-tuning is not required if using a well-matched pretrained model, but this choice must be explicitly stated.

## Hugging Face Sentiment Analysis Quickstart

A guide to running and fine-tuning transformer-based sentiment classifiers:

[Hugging Face: Sentiment Analysis with Python](https://huggingface.co/blog/sentiment-analysis-python)

## Mentor Reference Notes

A common shortcut is reporting only overall accuracy on an imbalanced dataset. Submissions should specifically be checked for per-class F1-scores before acceptance.
