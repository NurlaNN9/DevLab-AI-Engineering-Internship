# Required Task — Handwritten Digit Classifier with a CNN (MNIST)

**Category:** Programming  
**Task Type:** Required

---

## Task Overview

Train a convolutional neural network from scratch on MNIST, then prove it actually earns its architecture by comparing it against a plain MLP baseline trained under identical conditions.

You will also test the model against handwriting that never appeared in MNIST at all.

**The comparison and the real-world test are the assessed skill, not just hitting a high accuracy number.**

---

## Learning Objectives

- Load and normalize MNIST from a standard loader without a pre-built pipeline hiding the process.
- Build a CNN with at least two convolution + pooling blocks followed by a dense head, from scratch.
- Train the model while tracking train/validation loss and accuracy curves.
- Compare CNN performance against a plain MLP baseline trained on the same data, splits, and epochs.
- Generate and interpret a confusion matrix to identify which digits are most often confused.
- Save the trained model and reload it in a separate script to run inference on real handwritten images.

---

## Must-Have Features

### 1. Data Pipeline

MNIST loaded and normalized, with an explicit train/validation/test split.

The default test set must not be reused as validation data.

### 2. CNN Architecture

At least two convolution + pooling blocks followed by dense layers.

The architecture must be documented layer-by-layer in the README.

### 3. MLP Baseline

A plain fully connected network trained on the identical data, splits, and epoch count for a fair comparison.

### 4. Training Curves

Loss and accuracy plotted per epoch for both the CNN and the MLP.

### 5. Confusion Matrix

Computed on the test set, with a written note identifying the most-confused digit pair and a hypothesis for why.

### 6. Custom Image Test

The CNN must be tested on **5 real handwritten digit images** (photographed or drawn), not MNIST samples.

The preprocessing steps must be shown explicitly:

- Resize
- Grayscale
- Invert

### 7. Model Persistence

Trained weights must be saved to disk and reloaded in a separate script or cell to prove inference works without retraining.

### 8. Anti-Cheat: No Pretrained Weights

The CNN must be trained from random initialization.

Using a pretrained ImageNet backbone or transfer learning defeats the purpose of this task and will be rejected.

---

## Bonus Features

- Add data augmentation (rotation/shift) and show its effect on validation accuracy.
- Visualize the learned filters of the first convolutional layer.
- Add dropout/batch normalization and compare regularized vs. unregularized runs.
- Expose a small Flask/FastAPI endpoint that accepts an uploaded image and returns the predicted digit.

---

## Technical Requirements

| Technology | Requirement |
|---|---|
| PyTorch or TensorFlow/Keras | Either framework is accepted. State which one was used. |
| matplotlib | Required for plotting training curves and the confusion matrix. |
| CPU / Google Colab | CPU-only is sufficient. Google Colab's free tier is an acceptable option. |

---

## MNIST Dataset Reference

Official MNIST database description and download:

http://yann.lecun.com/exdb/mnist/

---

## Mentor Reference Notes

A simple CNN should reach roughly **99% test accuracy** on MNIST within a few epochs.

A result significantly below that should raise a flag before grading.

**The most common bug is forgetting to normalize pixel values.**
