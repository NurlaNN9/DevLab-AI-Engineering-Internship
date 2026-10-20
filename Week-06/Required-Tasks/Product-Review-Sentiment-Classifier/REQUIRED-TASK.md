# Product Review Sentiment Classifier

**svgSubmit task**

ProgrammingRequired

# Product Review Sentiment Classifier

Build a sentiment classifier for real product/service reviews that outputs positive/negative/neutral, and compare a classical ML baseline against a pretrained or fine-tuned transformer to show the trade-off between simplicity and performance. The genuine model comparison, on identical data splits, is the assessed skill - not accuracy alone.

## Learning objectives

- Clean and preprocess raw review text appropriately for the chosen method
- Build a classical ML baseline (TF-IDF plus Logistic Regression/SVM) trained on labeled review data
- Use a pretrained or fine-tuned transformer for the same classification task
- Evaluate both models with precision/recall/F1 per class, not accuracy alone, since review sentiment is often imbalanced
- Analyze misclassified examples to identify a systematic weakness (e.g. sarcasm, negation, mixed sentiment)
- Justify which model you would actually deploy given accuracy vs. latency/resource trade-offs

## Must-have features

- **Real Dataset** — A real-world review dataset (e.g. Amazon, Yelp, IMDb, or a small self-scraped set with permission) with at least 1,000 labeled examples.
- **Classical Baseline** — TF-IDF plus a classical classifier trained and evaluated.
- **Transformer Model** — A pretrained/fine-tuned transformer trained and evaluated on the identical train/test split as the baseline.
- **Per-Class Metrics** — Precision/recall/F1 reported per sentiment class for both models, not just overall accuracy.
- **Class Imbalance Handling** — The dataset's class imbalance is measured, and at least one mitigation (class weighting, resampling, or an explicit, reasoned decision to ignore it) is applied.
- **Error Analysis** — At least 5 misclassified examples reviewed with a written hypothesis for each about why the model got it wrong.
- **Model Comparison Verdict** — A written recommendation on which model to deploy for a stated hypothetical use case (e.g. real-time support triage vs. offline weekly reporting).
- **Anti-Cheat: Identical Splits** — Both models must be trained/evaluated on the exact same train/test split (same random seed or saved split file). Mismatched splits invalidate the comparison and will be rejected.

## Bonus features

- Add a neutral class if the dataset supports it and check whether it hurts binary performance
- Test both models on out-of-domain text (e.g. train on product reviews, test on restaurant reviews) to check generalization
- Build a simple confidence-calibration check - are high-confidence predictions actually more often correct?
- Wrap the better-performing model in a small CLI or API for live testing

## Technical requirements

- **scikit-learn** — For the classical baseline.
- **Hugging Face Transformers** — A free pretrained model (e.g. a DistilBERT sentiment model) or your own fine-tune is accepted - state which was used.
- **Sufficient compute for the transformer** — Google Colab's free-tier GPU is sufficient; a full fine-tune is not required if using a well-matched pretrained model, but this must be stated explicitly.

## Hugging Face sentiment analysis quickstart

A quickstart guide for running and fine-tuning transformer-based sentiment classifiers:

[https://huggingface.co/blog/sentiment-analysis-python](https://huggingface.co/blog/sentiment-analysis-python)

## Mentor reference notes

The common shortcut is reporting only overall accuracy on an imbalanced dataset - graders should specifically check for per-class F1 before accepting a submission.
