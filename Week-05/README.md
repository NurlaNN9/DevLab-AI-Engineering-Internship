# Week 5 — Real-Time Computer Vision

This week focuses on real-time computer vision: training a lightweight object detector and using it to recognize a pen or pencil in a live webcam stream.

## Required Task

### Real-Time Pen/Pencil Detector from Webcam Feed

The goal is to fine-tune a lightweight detector on a custom-labeled dataset, then run it continuously on webcam frames. The application uses OpenCV to capture video, draw bounding boxes and confidence scores, and display measured FPS. A configurable confidence threshold helps control detections and reduce false positives.

The project includes:

- A custom object-detection dataset with training and validation splits.
- YOLOv8n fine-tuning for pen/pencil detection.
- Webcam capture and per-frame inference using OpenCV.
- Live bounding boxes, class labels, confidence scores, and FPS.
- An adjustable confidence threshold.
- Held-out test-set evaluation.
- Live testing across different lighting and background conditions.
- Documented evaluation limitations.

## Technologies

- Python
- Ultralytics YOLOv8n
- OpenCV
- Google Colab
- LabelImg, Roboflow, or CVAT for dataset annotation

YOLOv8 supports training and inference for object-detection tasks. The project uses the fine-tuned checkpoint for webcam inference rather than relying on a generic pretrained detector alone. [132][2]

## Results

The notebook reports these results on its held-out test split:

| Metric | Test result |
|---|---:|
| Precision | 0.9508 |
| Recall | 0.9104 |
| mAP@50 | 0.9695 |
| mAP@50–95 | 0.6962 |

The notebook also contains three reported live-test FPS values. They have not been independently verified, so measure FPS again on the computer used for the final demonstration and update the table before submission.

| Condition | FPS in notebook (unverified) | Detection |
|---|---:|---|
| Normal light, plain background | 15.6 | Pen detected |
| Low light | 15.2 | Pen detected |
| Cluttered background | 14.8 | Pen detected |

The notebook notes several limitations: the test split contains only 40 images, some annotations may be incomplete, the test set has no background-only examples, and pencil detection still needs verification. Live performance may also vary with hardware, lighting, camera angle, and background.

## Project Structure

```text
Week-05/
├── README.md
└── Required-Tasks/
    └── Real-Time-Pen-Pencil-Detector/
        ├── dataset/
        ├── models/
        │   └── best.pt
        ├── real-time-pen-pencil-detector.ipynb
        ├── webcam_detector.py
        ├── README.md
        └── REQUIRED-TASK.md
```

The dataset and trained `best.pt` weights are not included in the upload because of their size. Add the dataset to `dataset/` and the trained model to `models/best.pt` before running the project.

## Run the Webcam Detector

Install the required packages:

```bash
pip install ultralytics opencv-python
```

Place the trained weights at:

```text
Required-Tasks/Real-Time-Pen-Pencil-Detector/models/best.pt
```

From the repository root, run:

```bash
python Required-Tasks/Real-Time-Pen-Pencil-Detector/webcam_detector.py
```

Press `Q` to quit. Press `+` or `=` to raise the confidence threshold, and `-` to lower it.

## Task Specification

The full task description is preserved in:

```text
Required-Tasks/Real-Time-Pen-Pencil-Detector/REQUIRED-TASK.md
```
