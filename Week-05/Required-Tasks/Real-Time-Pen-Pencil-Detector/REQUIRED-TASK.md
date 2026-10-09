# Real-Time Pen/Pencil Detector from Webcam Feed

Train or fine-tune a lightweight detector to recognize a pen or pencil in a live webcam stream and draw a bounding box in real time, across varying lighting, angle, and background. Real-time inference has constraints - speed, jitter, false positives - that static-image detection in Week 3 never surfaced; this is the first task that must run continuously and stay usable, not just produce one correct answer per image.

## Learning objectives

* Collect or source a small labeled dataset of pen/pencil images across varied backgrounds and angles
* Fine-tune a lightweight object detector for a single custom class
* Read frames from a webcam stream and run inference per frame at an acceptable latency, reporting FPS
* Draw bounding boxes and confidence scores overlaid on the live video feed
* Reduce false positives from background clutter using confidence thresholding and/or temporal smoothing across frames
* Evaluate real-world performance live, not just on a held-out test set, and document where it breaks

## Must-have features

* **Custom Dataset** — At least 100 labeled pen/pencil images (self-collected or a small public subset), with a clear train/validation split.
* **Fine-Tuned Detector** — A single-class detector trained specifically on pen/pencil, not a generic pretrained model that merely happens to have a similar class.
* **Live Webcam Loop** — An OpenCV video capture loop running inference per frame with bounding boxes drawn live on screen.
* **FPS Reporting** — Frames-per-second measured and displayed during live inference, not just a theoretical model speed figure.
* **Confidence Thresholding** — A configurable threshold that visibly reduces false-positive boxes when raised.
* **Lighting/Background Robustness Test** — A short demonstration (video clip or documented test) across at least 3 different lighting/background conditions, with results noted.

**Anti-Cheat: Trained Model Required** — A color-thresholding or edge-detection heuristic (e.g. 'find thin dark rectangles') does not satisfy this task. The detector must be a trained model whose weights the mentor can inspect.

## Bonus features

* Add a second custom class (e.g. pen vs. highlighter) and report per-class accuracy
* Add temporal smoothing across frames to reduce box flicker
* Trigger a sound/action when a pen is detected for N consecutive frames
* Deploy the detector on a Raspberry Pi or mobile device and report the FPS difference

## Technical requirements

* **OpenCV** — For video capture and drawing.
* **Ultralytics YOLOv8 or a custom lightweight CNN** — YOLOv8 is recommended for fine-tuning speed; a sliding-window CNN is an acceptable fallback - state which and why.
* **A labeling tool** — LabelImg, Roboflow, or CVAT for the custom dataset.

## Roboflow/LabelImg quickstart

A quickstart guide for labeling custom object-detection datasets: https://roboflow.com/annotate

## Mentor reference notes

A few frames per second on a laptop CPU without a GPU is expected and acceptable - the point of this task is understanding the speed/accuracy trade-off, not hitting 60 FPS.
