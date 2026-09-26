# License Plate Detection and Recognition Pipeline

**Submit task**

ProgrammingRequired

# License Plate Detection and Recognition Pipeline

Build an end-to-end pipeline that detects a license plate in a vehicle image and reads the plate text using OCR, evaluating both stages against ground truth on a held-out test set. This is the program's first task chaining two different models into one working pipeline, instead of one model doing everything - the hand-off between detector and recognizer is the assessed skill.

## Learning objectives

- Use or fine-tune an object detection model specifically for the 'license plate' class
- Crop the detected plate region correctly, handling images with multiple or zero detections
- Apply OCR to the cropped plate region and clean the raw text output
- Evaluate detection quality with IoU-based metrics against ground-truth boxes
- Evaluate OCR quality with exact-match and character-error-rate against ground-truth plate strings
- Handle real-world failure modes: blurry plates, angled plates, partial occlusion
- Package the two stages into one callable pipeline function (image in, plate text out)

## Must-have features

- **Detector Model** — A trained, fine-tuned, or configured detection model that outputs bounding boxes for plates on a labeled test set.
- **Ground-Truth Evaluation** — IoU computed against at least 20 hand-labeled test images, with mean IoU reported.
- **Plate Cropping** — Correct crop extraction with padding, tested on at least 3 images containing multiple vehicles.
- **OCR Integration** — Tesseract or EasyOCR applied to each crop, with the raw text output captured.
- **Text Cleaning** — Post-processing removes OCR noise using at least one rule-based correction (e.g. 0/O or 1/I disambiguation for the local plate format).
- **End-to-End Accuracy Report** — A table of image -> detected box -> OCR text -> correct/incorrect, with overall accuracy reported.
- **Failure Case Analysis** — At least 3 example failures shown and explained (why the detector or the OCR step failed).
- **Anti-Cheat: No Manual Cropping** — Detection boxes must come from the model's own output, not hand-drawn coordinates. The mentor will re-run the pipeline on 3 unseen images to confirm the detector genuinely works.

## Bonus features

- Extend to real-time video (webcam or dashcam footage) with bounding boxes drawn live
- Add plate-format validation via regex for the local plate format
- Build a small log/database that records detected plates with a timestamp, like a mini parking log
- Compare Tesseract vs. EasyOCR accuracy on the identical test set

## Technical requirements

- **OpenCV** — For image handling and drawing.
- **A detection framework** — Ultralytics YOLOv8 is recommended for ease of fine-tuning; an OpenCV Haar cascade is an acceptable lighter fallback - state which was used and why.
- **Tesseract-OCR or EasyOCR** — Tesseract needs a system install; EasyOCR is pip-only but a heavier download - name whichever escape hatch was needed.
- **A small labeled dataset** — A public license plate dataset, or 30-50 self-photographed images labeled with a tool such as LabelImg or Roboflow.

## Ultralytics YOLOv8 quickstart

Official quickstart and fine-tuning documentation for YOLOv8: [https://docs.ultralytics.com/quickstart/](https://docs.ultralytics.com/quickstart/)

## Mentor reference notes

Interns most often get stuck on labeling-format mismatches between annotation tools, and on Tesseract path/config issues on Windows - check these first if a submission reports it 'doesn't work'.
