# Real-Time Pen/Pencil Detector

A YOLOv8n-based project for detecting pens or pencils in a webcam stream. The training and evaluation workflow is in `real-time-pen-pencil-detector.ipynb`; the live camera application is `webcam_detector.py`.

## Folders and Files

- `real-time-pen-pencil-detector.ipynb`: Prepares the dataset, fine-tunes YOLOv8n, and evaluates the model.
- `webcam_detector.py`: Runs live webcam inference with OpenCV and displays bounding boxes, class confidence, live FPS, and an adjustable confidence threshold.
- `models/best.pt`: Place your trained model weights here. The large file is not included in the ZIP.
- `dataset/`: Place the dataset files here. The dataset is not included in the ZIP.
- `REQUIRED-TASK.md`: Contains the original task description.

## Run the Detector

Python 3.10 or 3.11 is recommended. Open a terminal in the project folder and install the dependencies:

```bash
pip install ultralytics opencv-python
```

Place the trained `best.pt` file at `models/best.pt`, then run:

```bash
python webcam_detector.py
```

Press `Q` to quit. Press `+` or `=` to raise the confidence threshold, and `-` to lower it. If the webcam does not open, the application falls back to the default camera API. If needed, change `CAMERA_INDEX` in `webcam_detector.py`. The code is configured to run on the CPU.

## Dataset and Attribution

The notebook prompts you to upload a YOLO-format dataset ZIP to `/content`. Specify the dataset source and license here; the dataset files are not included in the project ZIP. The notebook checks for empty or missing labels, prepares the single-class training setup, and evaluates `best.pt` on the test split.

## Evaluation Notes

The notebook reports the following results on 40 test images: Precision 0.9508, Recall 0.9104, mAP@50 0.9695, and mAP@50–95 0.6962. It also notes that some annotations may be incomplete, the test split is small, it contains no background-only examples, and pencil detection has not been verified.

The notebook lists FPS values of 15.6, 15.2, and 14.8 for three live-test conditions. These values have not been independently verified; measure them again on your own computer and update the results accordingly. FPS varies with hardware, resolution, and camera conditions. Add observations from lighting and background tests you have actually performed.

## Limitations

- The model targets one custom class. Verify the class name and label coverage against your dataset.
- Static test metrics do not guarantee webcam performance in new environments.
- The model weights and dataset are not included in this delivery because of their size. Add your own files to the specified folders.
