# Handwritten Digit Classifier with a CNN (MNIST)

A handwritten digit classification project developed as the **Week 02 Required Task** for the DevLab AI Engineering Internship.

The project uses **PyTorch**, **Torchvision**, and the **MNIST dataset** to train a convolutional neural network (CNN) from scratch, compare it against a multilayer perceptron (MLP), and classify handwritten digits created outside MNIST.

## Project Overview

The project focuses on training and evaluating neural networks for handwritten digit classification.

Two models are developed from scratch:

- Convolutional Neural Network (CNN)
- Multilayer Perceptron (MLP)

Both models are trained using the same dataset splits, number of epochs, optimizer, and learning rate.

The trained CNN is then evaluated on the MNIST test dataset and five handwritten digit images created separately.

Additional experiments explore image preprocessing, data augmentation, and learned convolutional filters.

## Model Architecture

```text
MNIST Dataset
       │
       ▼
Data Normalization
       │
       ▼
Train / Validation / Test Split
       │
       ├────────────────────────────┐
       │                            │
       ▼                            ▼
   CNN Model                    MLP Model
       │                            │
       ▼                            ▼
Convolution + ReLU             Flatten
       │                            │
       ▼                            ▼
   Max Pooling               Dense Layers
       │                            │
       ▼                            │
Convolution + ReLU                  │
       │                            │
       ▼                            │
   Max Pooling                      │
       │                            │
       ▼                            │
  Dense Layers                      │
       │                            │
       └──────────────┬─────────────┘
                      │
                      ▼
             Model Evaluation
                      │
                      ▼
             CNN Confusion Matrix
                      │
                      ▼
          Custom Handwriting Test
                      │
                      ▼
          Preprocessing Comparison
```

### CNN Architecture

The CNN contains two convolution and pooling blocks followed by fully connected layers.

| Layer | Output Shape | Purpose |
|---|---|---|
| Input | 1 × 28 × 28 | Grayscale image |
| Conv2D + ReLU | 32 × 28 × 28 | Learn local visual patterns |
| MaxPool2D | 32 × 14 × 14 | Reduce spatial dimensions |
| Conv2D + ReLU | 64 × 14 × 14 | Learn more complex features |
| MaxPool2D | 64 × 7 × 7 | Reduce spatial dimensions |
| Flatten | 3136 | Prepare features for dense layers |
| Linear + ReLU | 128 | Combine learned features |
| Linear | 10 | Classification scores for digits 0–9 |

### MLP Architecture

The MLP processes flattened images using fully connected layers:

```text
Input Image (28 × 28)
        │
        ▼
      Flatten
        │
        ▼
   784 Features
        │
        ▼
 Linear (784 → 128)
        │
        ▼
       ReLU
        │
        ▼
 Linear (128 → 64)
        │
        ▼
       ReLU
        │
        ▼
 Linear (64 → 10)
        │
        ▼
  Predicted Digit
```

Unlike the CNN, the MLP does not use convolution or pooling layers.

## Features

- MNIST dataset loading through Torchvision
- Pixel normalization to the [0, 1] range
- Explicit training, validation, and test splits
- CNN architecture with two convolution and pooling blocks
- Fully connected MLP baseline
- Training from random initialization without pretrained weights
- Fair model comparison under identical training conditions
- Training and validation loss tracking
- Training and validation accuracy tracking
- Performance visualization using Matplotlib
- CNN confusion matrix
- Classification of five custom handwritten digits
- Original and improved image preprocessing
- Model saving and reloading
- Inference without retraining
- Data augmentation experiment
- Convolutional filter visualization

## Dataset and Training

The project uses the **MNIST handwritten digit dataset**, containing 70,000 grayscale images of digits from 0 to 9.

Each image has a resolution of 28 × 28 pixels.

Images are converted into tensors using `transforms.ToTensor()`, which scales pixel values from 0–255 to the [0, 1] range.

### Dataset Split

| Dataset | Images |
|---|---:|
| Training | 54,000 |
| Validation | 6,000 |
| Test | 10,000 |

The original MNIST training dataset is divided into separate training and validation datasets.

The official MNIST test dataset is kept separate for final evaluation.

### Training Configuration

| Parameter | Value |
|---|---|
| Framework | PyTorch |
| Epochs | 5 |
| Batch Size | 64 |
| Learning Rate | 0.001 |
| Optimizer | Adam |
| Loss Function | CrossEntropyLoss |

Both the CNN and MLP use the same training and validation datasets, epoch count, optimizer, and learning rate.

## Model Performance

Both models were evaluated on the MNIST test dataset after training.

| Model | Final Validation Accuracy | Test Accuracy |
|---|---:|---:|
| CNN | 98.58% | 98.82% |
| MLP | 96.68% | 97.31% |
| CNN + Augmentation | 98.82% | 99.01% |

The original CNN achieved **98.82% test accuracy**, compared to **97.31%** for the MLP.

The CNN performed better on the MNIST test dataset by **1.51 percentage points**.

The augmented CNN achieved the highest test accuracy in this experiment, reaching **99.01%**.

## Confusion Matrix

A confusion matrix was generated using the original CNN's predictions on the MNIST test dataset.

The CNN correctly classified **9,882 out of 10,000 images**.

The most frequent directional classification error was:

| Actual Digit | Predicted Digit | Mistakes |
|---|---|---:|
| 8 | 9 | 10 |

One possible explanation is that some handwritten 8s have an unclear lower loop, making them visually similar to 9s.

The confusion matrix and its interpretation are included in the notebook.

## Custom Handwriting Test

The trained CNN was tested on five handwritten digit images created outside MNIST.

The images contain the following digits:

**0, 2, 4, 6, and 9**

These images were not used during model training.

### Original Preprocessing

The original preprocessing method:

- Converts the image to grayscale
- Inverts the colors to match MNIST
- Resizes the entire image to 28 × 28 pixels
- Converts the processed image into a tensor

The CNN initially predicted **2 out of 5 digits correctly (40%)**.

### Improved Preprocessing

The preprocessing was improved by:

- Cropping the empty background
- Resizing the digit to fit within 20 × 20 pixels
- Preserving the digit's aspect ratio
- Centering the digit on a black 28 × 28 canvas

### Preprocessing Results

| Preprocessing | Correct Predictions | Accuracy |
|---|---:|---:|
| Original | 2/5 | 40% |
| Improved | 5/5 | 100% |

The same CNN and the same five images were used in both tests.

**The model was not retrained.**

This experiment demonstrates how image preprocessing can affect classification results.

However, five images are a small sample, so the 100% result does not represent general accuracy on all real-world handwriting.

## Model Persistence

The trained CNN weights were saved using PyTorch.

The saved weights were then loaded into a new CNN instance to perform inference without retraining.

The model is available in:

`models/cnn_mnist.pth`

## Additional Experiments

### Data Augmentation

A separate CNN was trained using augmented MNIST training images.

The augmentation included:

- Random rotations of up to 10 degrees
- Horizontal shifts of up to 10%
- Vertical shifts of up to 10%

The validation and test datasets were not augmented.

The augmented CNN achieved **99.01% test accuracy**, compared to **98.82%** for the original CNN.

### Convolutional Filter Visualization

The learned filters from the first convolutional layer were extracted and visualized.

The first convolutional layer contains:

- 32 filters
- 1 input channel
- 3 × 3 filter dimensions

The visualization shows different weight patterns learned during training.

These filters can help the CNN detect simple visual features such as lines and edges.

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
- Git & GitHub

## Project Files

```text
Handwritten-Digit-Classifier/
│
├── README.md
├── Week02_MNIST_CNN_vs_MLP.ipynb
│
├── documentation/
│   └── EXPERIMENT-NOTES.md
│
├── models/
│   └── cnn_mnist.pth
│
└── handwritten-digits/
    ├── digit_0.png
    ├── digit_2.png
    ├── digit_4.png
    ├── digit_6.png
    └── digit_9.png
```

The original task description is stored in:

`../REQUIRED-TASK.md`

The MNIST `data/` directory is generated automatically and is not included in the repository.

## Testing

The project was tested through several scenarios, including:

- CNN training and validation
- MLP training and validation
- CNN and MLP test evaluation
- Confusion matrix analysis
- Model saving and reloading
- Inference using saved model weights
- Five custom handwritten digit predictions
- Improved preprocessing comparison
- Data augmentation comparison
- Convolutional filter visualization

The executed notebook contains the training results, plots, and prediction outputs.

## Running the Project

The project was developed using Google Colab.

To reproduce the experiments:

1. Open `Week02_MNIST_CNN_vs_MLP.ipynb` in Google Colab.
2. Make the model weights and custom handwritten images available in the working directory.
3. Run the notebook cells in order.

MNIST downloads automatically through Torchvision.

The saved CNN weights can also be loaded separately for inference without repeating the training process.

## Project Documentation

- [Original Required Task](../REQUIRED-TASK.md)
- [Jupyter Notebook](Week02_MNIST_CNN_vs_MLP.ipynb)
- [Experiment Notes](documentation/EXPERIMENT-NOTES.md)
- [Custom Handwritten Images](handwritten-digits/)
- [Saved CNN Model](models/cnn_mnist.pth)

---

**DevLab AI Engineering Internship — Week 02 Required Task**
