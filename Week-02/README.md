# Week 02 — Computer Vision with PyTorch

This directory contains the tasks, implementations, model files, experiments, and documentation completed during **Week 02** of the DevLab AI Engineering Internship.

Week 02 focuses on image classification using neural networks, model evaluation, and image preprocessing.

## Week 02 Structure

```text
Week-02/
│
├── Required-Tasks/
│   ├── README.md
│   └── Handwritten-Digit-Classifier/
│       ├── documentation/
│       ├── handwritten-digits/
│       ├── models/
│       ├── Week02_MNIST_CNN_vs_MLP.ipynb
│       ├── README.md
│       └── REQUIRED-TASK.md
│
└── README.md
```

## Required Task

### Handwritten Digit Classifier with a CNN (MNIST)

A handwritten digit classification project built with **PyTorch, Torchvision, NumPy, Matplotlib, scikit-learn, and Pillow**.

The project:

- Loads and normalizes the MNIST dataset
- Creates separate training, validation, and test datasets
- Builds a CNN from scratch with two convolution and pooling blocks
- Builds a fully connected MLP baseline
- Trains both models using the same data splits and epoch count
- Tracks training and validation loss and accuracy
- Visualizes and compares the training curves
- Evaluates both models on the MNIST test dataset
- Generates a confusion matrix for the CNN
- Identifies and explains the most common digit confusion
- Tests the CNN on five custom handwritten digit images
- Improves image preprocessing for real handwritten digits
- Saves and reloads the trained CNN weights for inference without retraining

Project directory:

`Required-Tasks/Handwritten-Digit-Classifier/`

---

## Model Performance

Both the original CNN and the MLP were trained for **5 epochs** using the same training and validation datasets.

| Model | Validation Accuracy | Test Accuracy |
|---|---:|---:|
| CNN | 98.58% | 98.82% |
| MLP | 96.68% | 97.31% |
| CNN + Augmentation | 98.82% | 99.01% |

The CNN achieved higher test accuracy than the MLP under the same training conditions.

The most common confusion was predicting digit **8 as 9**, which happened **10 times**.

---

## Custom Handwriting Experiment

The trained CNN was tested on five handwritten digit images created outside the MNIST dataset.

The digits were:

**0, 2, 4, 6, and 9**

The initial preprocessing converted the images to grayscale, inverted their colors, and resized them to 28×28 pixels.

After the first test, preprocessing was improved by:

- Cropping the empty background
- Resizing each digit while preserving its aspect ratio
- Centering the digit on a 28×28 canvas

| Preprocessing Method | Correct Predictions | Accuracy |
|---|---:|---:|
| Original preprocessing | 2/5 | 40% |
| Improved preprocessing | 5/5 | 100% |

The CNN was not retrained between these tests.

The experiment demonstrates how image preprocessing can affect model predictions. However, five images are a small sample and do not establish general accuracy on real-world handwriting.

---

## Additional Experiments

### Experiment 01 — Data Augmentation

A second CNN was trained using small rotations and shifts applied to the training images.

The experiment:

- Applies random rotations of up to 10 degrees
- Applies horizontal and vertical shifts
- Keeps the validation and test datasets unchanged
- Uses the same CNN architecture and training settings
- Compares validation accuracy with the original CNN

The augmented CNN achieved **99.01% test accuracy**, compared to **98.82%** for the original CNN.

### Experiment 02 — Convolutional Filter Visualization

The learned filters from the first convolutional layer were visualized.

The experiment:

- Extracts the trained weights from the first convolutional layer
- Visualizes all 32 learned filters
- Shows the 3×3 filter weight patterns
- Helps explore how convolutional layers learn visual features

Both experiments are documented in the required project's notebook and supporting documentation.

---

## Week 02 Completed Work

- **1 Required Task** — Handwritten Digit Classifier with a CNN (MNIST)
- CNN and MLP trained from scratch
- Training and validation curves
- Test evaluation and confusion matrix
- Five custom handwritten digit images
- Original and improved preprocessing comparison
- Saved CNN model weights
- Model reload and inference
- Data augmentation experiment
- Convolutional filter visualization
- Jupyter notebook with executed results
- Technical documentation and experiment notes

## Technologies Used

- Python
- PyTorch
- Torchvision
- NumPy
- Pandas
- Matplotlib
- scikit-learn
- Pillow
- Google Colab
- MNIST Dataset

---

**DevLab AI Engineering Internship — Week 02**
