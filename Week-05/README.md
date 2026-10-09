# Week 5 — Real-Time Computer Vision

This week focuses on real-time computer vision: training lightweight computer vision models and running inference on live or continuous visual input.

## Required Task

### Real-Time Pen/Pencil Detector from Webcam Feed

The required project is a real-time object detector that recognizes a pen or pencil from a live webcam stream.

The project fine-tunes a lightweight YOLOv8n detector on a custom-labeled dataset and runs inference continuously on webcam frames. OpenCV is used to capture frames, draw bounding boxes and confidence scores, and display measured frames per second (FPS).

The project includes:

- A custom object-detection dataset with training and validation splits.
- YOLOv8n fine-tuning for pen/pencil detection.
- Webcam capture and per-frame inference using OpenCV.
- Live bounding boxes, class labels, confidence scores, and FPS display.
- An adjustable confidence threshold for reducing false positives.
- Held-out test-set evaluation.
- Live testing across different lighting and background conditions.
- Documented evaluation limitations.

## Technologies

- Python
- Ultralytics YOLOv8n
- OpenCV
- Google Colab
- LabelImg, Roboflow, or CVAT for dataset annotation

## Results

The notebook reports the following results on its held-out test split:

| Metric | Test Result |
|---|---:|
| Precision | 0.9508 |
| Recall | 0.9104 |
| mAP@50 | 0.9695 |
| mAP@50–95 | 0.6962 |

The notebook includes the following recorded FPS values for live webcam tests:

| Condition | FPS | Detection |
|---|---:|---|
| Normal light, plain background | 15.6 | Pen detected |
| Low light | 15.2 | Pen detected |
| Cluttered background | 14.8 | Pen detected |

The test split contains 40 images. The project documentation notes that some annotations may be incomplete, the test set contains no background-only examples, and pencil detection requires further verification. Live performance may vary depending on hardware, lighting, camera angle, resolution, and background complexity.

## Bonus Tasks

Additional computer-vision tasks may be added to this week after completion. These tasks will be documented here with their project name, purpose, technologies, results, and repository path.

## Project Structure

```text
Week-05/
├── README.md
└── Required-Tasks/
    └── Real-Time-Pen-Pencil-Detector/
        ├── dataset/
        │   └── README.md
        ├── models/
        │   └── best.pt
        ├── real-time-pen-pencil-detector.ipynb
        ├── webcam_detector.py
        ├── README.md
        └── REQUIRED-TASK.md
```

The dataset and trained `best.pt` weights are not included in the repository because of their size. Add the dataset to `dataset/` and the trained model to `models/best.pt` before running the project.

## Run the Webcam Detector

Install the required packages:

```bash
pip install ultralytics opencv-python
```

Place the trained model weights at:

```text
Required-Tasks/Real-Time-Pen-Pencil-Detector/models/best.pt
```

From the repository root, run:

```bash
python Required-Tasks/Real-Time-Pen-Pencil-Detector/webcam_detector.py
```

Press `Q` to quit. Press `+` or `=` to increase the confidence threshold, and `-` to decrease it.

## Task Specification

The complete task specification is available at:

```text
Required-Tasks/Real-Time-Pen-Pencil-Detector/REQUIRED-TASK.md
```
