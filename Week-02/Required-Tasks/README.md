# Handwritten Digit Classifier with a CNN (MNIST)

A handwritten digit classification project developed as the **Week 02 Required Task** for the DevLab AI Engineering Internship.

The project uses **PyTorch** to train a convolutional neural network (CNN) from scratch on the MNIST dataset and compares its performance with a fully connected multilayer perceptron (MLP).

The trained CNN is also tested on five custom handwritten digit images to evaluate its performance on images outside the MNIST dataset.

## Project Overview

The main objective is to understand how convolutional neural networks work and evaluate whether their architecture provides an advantage over a plain fully connected neural network for image classification.

The project includes:

- MNIST dataset loading and normalization
- Explicit training, validation, and test splits
- CNN architecture built from scratch
- MLP baseline trained under the same conditions
- Training and validation performance tracking
- Confusion matrix analysis
- Custom handwritten digit classification
- Image preprocessing experiments
- Model saving and reloading
- Data augmentation
- Convolutional filter visualization

All models were trained from random initialization without pretrained weights.

## Model Architecture

### Convolutional Neural Network (CNN)

The CNN contains two convolution and pooling blocks followed by fully connected layers.

```text
Input Image
  1 × 28 × 28
       │
       ▼
Conv2D (1 → 32, 3×3)
       │
       ▼
ReLU
       │
       ▼
MaxPool2D (2×2)
  32 × 14 × 14
       │
       ▼
Conv2D (32 → 64, 3×3)
       │
       ▼
ReLU
       │
       ▼
MaxPool2D (2×2)
   64 × 7 × 7
       │
       ▼
Flatten
   3136 Features
       │
       ▼
Linear (3136 → 128)
       │
       ▼
ReLU
       │
       ▼
Linear (128 → 10)
       │
       ▼
Predicted Digit
      0–9
```

### CNN Layer Details

| Layer | Output Shape | Purpose |
|---|---|---|
| Input | 1 × 28 × 28 | Grayscale MNIST image |
| Conv2D + ReLU | 32 × 28 × 28 | Learn local visual patterns |
| MaxPool2D | 32 × 14 × 14 | Reduce spatial dimensions |
| Conv2D + ReLU | 64 × 14 × 14 | Learn more complex features |
| MaxPool2D | 64 × 7 × 7 | Reduce spatial dimensions |
| Flatten | 3136 | Convert feature maps into a vector |
| Linear + ReLU | 128 | Learn classification patterns |
| Linear | 10 | Produce scores for digits 0–9 |

### Multilayer Perceptron (MLP)

The MLP is used as a baseline for comparison.

```text
Input Image
  28 × 28
     │
     ▼
Flatten
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
    0–9
```

Unlike the CNN, the MLP processes flattened pixel values without convolution or pooling layers.

## Dataset and Preprocessing

The project uses the **MNIST handwritten digit dataset**.

MNIST contains 70,000 grayscale images of handwritten digits from 0 to 9.

Each image has a resolution of 28 × 28 pixels.

### Dataset Split

| Dataset | Images |
|---|---:|
| Training | 54,000 |
| Validation | 6,000 |
| Test | 10,000 |
| Total | 70,000 |

The original MNIST training dataset was divided into separate training and validation datasets.

The official test dataset was kept separate for final evaluation.

### Normalization

Images were converted into PyTorch tensors using `transforms.ToTensor()`.

This converts pixel values from the original 0–255 range into the 0–1 range.

The same dataset split was used for both the CNN and MLP.

## Training Configuration

Both models were trained using the same main settings.

| Parameter | Value |
|---|---|
| Framework | PyTorch |
| Epochs | 5 |
| Batch Size | 64 |
| Learning Rate | 0.001 |
| Optimizer | Adam |
| Loss Function | CrossEntropyLoss |
| Training Images | 54,000 |
| Validation Images | 6,000 |
| Test Images | 10,000 |

Training and validation loss and accuracy were recorded for every epoch.

The notebook includes visualizations of these metrics for both models.

## Model Performance

### Final Results

| Model | Final Validation Accuracy | Test Accuracy |
|---|---:|---:|
| CNN | 98.58% | 98.82% |
| MLP | 96.68% | 97.31% |
| CNN + Augmentation | 98.82% | 99.01% |

The original CNN achieved **98.82% test accuracy**, compared to **97.31%** for the MLP.

The difference was **1.51 percentage points** in favor of the CNN on the MNIST test dataset.

The results demonstrate the advantage of convolutional layers for learning local image patterns in this experiment.

## Confusion Matrix

A confusion matrix was generated using the CNN predictions on the MNIST test dataset.

The original CNN correctly classified **9,882 out of 10,000** test images.

The most common classification error was:

| Actual Digit | Predicted Digit | Mistakes |
|---|---|---:|
| 8 | 9 | 10 |

One possible explanation is that some handwritten 8s have an incomplete or unclear lower loop, making them visually similar to 9s.

The confusion matrix and its interpretation are included in the notebook.

## Custom Handwriting Experiment

The trained CNN was tested on five handwritten digit images created outside the MNIST dataset.

The custom digits were:

**0, 2, 4, 6, and 9**

The images were created separately and were not used during model training.

### Original Preprocessing

The first preprocessing method:

1. Converted the image to grayscale
2. Inverted the colors
3. Resized the entire image to 28 × 28 pixels
4. Converted the image into a tensor

### Original Results

| Actual Digit | Predicted Digit | Correct |
|---|---|---|
| 0 | 9 | No |
| 2 | 3 | No |
| 4 | 4 | Yes |
| 6 | 5 | No |
| 9 | 9 | Yes |

**Accuracy: 2/5 — 40%**

The model performed significantly worse on these custom images than on MNIST.

One possible reason was the difference in digit size and positioning.

### Improved Preprocessing

A second preprocessing method was tested using the same five images.

The improved method:

1. Converts the image to grayscale
2. Inverts the colors
3. Crops the empty background
4. Resizes the digit while preserving its aspect ratio
5. Centers the digit on a 28 × 28 black canvas
6. Converts the processed image into a tensor

### Improved Results

| Preprocessing | Correct Predictions | Accuracy |
|---|---:|---:|
| Original | 2/5 | 40% |
| Improved | 5/5 | 100% |

The model was **not retrained** between the two tests.

This experiment shows that image preprocessing can strongly affect predictions on handwritten images.

However, five images are a small sample, so the 100% result should not be interpreted as general accuracy on all real-world handwriting.

## Model Persistence

The trained CNN weights were saved using PyTorch.

```python
torch.save(cnn.state_dict(), "cnn_mnist.pth")
```

The saved weights were then loaded into a new CNN instance.

```python
loaded_cnn = CNN().to(device)

loaded_cnn.load_state_dict(
    torch.load(
        "cnn_mnist.pth",
        map_location=device,
        weights_only=True
    )
)

loaded_cnn.eval()
```

The reloaded model successfully performed inference without retraining.

The trained weights are included in the `models/` directory.

## Additional Experiments

### Experiment 01 — Data Augmentation

A second CNN was trained using augmented MNIST training images.

The augmentation included:

- Random rotations of up to 10 degrees
- Small horizontal shifts
- Small vertical shifts

The validation and test datasets remained unchanged.

The augmented CNN used the same architecture, epoch count, optimizer, and learning rate as the original CNN.

| Model | Final Validation Accuracy | Test Accuracy |
|---|---:|---:|
| Original CNN | 98.58% | 98.82% |
| CNN + Augmentation | 98.82% | 99.01% |

The augmented CNN achieved a slightly higher validation and test accuracy in this experiment.

### Experiment 02 — Convolutional Filter Visualization

The learned weights from the first convolutional layer were extracted and visualized.

The first convolutional layer contains:

- 32 filters
- 1 input channel
- 3 × 3 filter dimensions

The visualization shows the different weight patterns learned during training.

These filters can help the CNN detect simple visual features such as lines and edges.

Both additional experiments are included in the notebook.

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
├── REQUIRED-TASK.md
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

## Running the Project

The project was developed and executed using Google Colab.

To reproduce the experiments:

1. Open `Week02_MNIST_CNN_vs_MLP.ipynb` in Google Colab.
2. Make the saved model weights and custom handwritten images available in the notebook's working environment.
3. Run the notebook cells in order.
4. Train and evaluate the CNN and MLP.
5. Generate the training curves and confusion matrix.
6. Test the reloaded CNN on the custom handwritten images.
7. Run the additional experiments.

MNIST is downloaded automatically through Torchvision.

The saved model weights can also be loaded separately for inference without repeating the training process.

## Project Documentation

- [Original Required Task](REQUIRED-TASK.md)
- [Jupyter Notebook](Week02_MNIST_CNN_vs_MLP.ipynb)
- [Experiment Notes](documentation/EXPERIMENT-NOTES.md)
- [Custom Handwritten Images](handwritten-digits/)
- [Saved CNN Model](models/cnn_mnist.pth)

---

**DevLab AI Engineering Internship — Week 02 Required Task**
