# License Plate Detection and Recognition Pipeline

## Project Overview

This project builds an end-to-end license plate recognition pipeline using YOLOv8 and EasyOCR.

The system first detects license plates in vehicle images, extracts the detected regions with padding, and then sends the crops to EasyOCR. The OCR output is cleaned before evaluation.

## Pipeline

```text
Vehicle Image
     |
     v
YOLOv8 Detector
     |
     v
License Plate Box
     |
     v
Plate Crop + Padding
     |
     v
EasyOCR
     |
     v
Text Cleaning
     |
     v
Recognized Plate Text
```

## Detection Model

YOLOv8 Nano was fine-tuned on the Roboflow License Plates v3 dataset.

Validation results for the license-plate class:

- Precision: 93.7%
- Recall: 88.1%
- mAP@50: 92.2%
- mAP@50-95: 68.7%

## Evaluation

The held-out test set is used for final evaluation.

- Mean test IoU: 74.78%
- OCR ground-truth images: 22
- End-to-end exact-match accuracy: 22.73%
- Mean character error rate (CER): 0.7718

The notebook also includes multiple-vehicle examples and failure-case analysis.

## Text Cleaning

OCR output is converted to uppercase and non-alphanumeric characters are removed. A configurable plate-format cleaner also supports common `0/O` and `1/I` corrections when the expected character type is known.

## Technologies Used

- Python
- Ultralytics YOLOv8
- EasyOCR
- OpenCV
- PyTorch
- Pandas
- Matplotlib
- Google Colab

## Project Files

```text
License-Plate-Detection-and-Recognition-Pipeline/
├── documentation/
├── models/
├── README.md
└── Week03_License_Plate_Detection_OCR.ipynb
```

## Dataset

Roboflow Universe — License Plates v3 by Samrat Sahoo  
License: CC BY 4.0  
Dataset page: https://universe.roboflow.com/samrat-sahoo/license-plates-f8vsn/dataset/3

The private Roboflow download token is not stored in the repository.

## Model File

The trained YOLOv8 weights are included in `models/best.pt`.
