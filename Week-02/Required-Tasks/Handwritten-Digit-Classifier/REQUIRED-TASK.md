# Required Task — Handwritten Digit Classifier with a CNN (MNIST)

## Goal
Train a CNN from scratch on MNIST, compare it with an MLP baseline, and test the trained CNN on five handwritten images created outside MNIST.

## Required work completed

- Load and normalize MNIST; split into 54,000 training, 6,000 validation and 10,000 test images.
- Build and document a CNN with two convolution + pooling blocks and a dense classification head.
- Train an MLP baseline with the same split, epochs, optimizer and learning rate.
- Plot training/validation loss and accuracy for both models.
- Evaluate on the test set; inspect a confusion matrix and discuss the most frequent directional confusion (8 → 9, 10 images).
- Test five original handwritten digit PNGs and document grayscale/invert/resize preprocessing.
- Compare initial custom-image accuracy (2/5) with improved crop/center preprocessing (5/5) using the same trained CNN.
- Save and reload the CNN weights for inference without retraining.

## Extra work completed

- Visualize the 32 learned filters in the first convolutional layer.
- Train and compare a CNN with small random rotations and shifts (99.01% test accuracy).

## Deliverables

See [README.md](README.md) for architecture, results and instructions. The [notebook](Week02_MNIST_CNN_vs_MLP.ipynb), [saved model](models/cnn_mnist.pth), and [handwritten images](handwritten-digits/) are included.
