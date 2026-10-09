# Dataset

The dataset files are not included in this repository because of their size.

## Download Links

- Google Drive: [Download the dataset ZIP](https://drive.google.com/file/d/1a-z-ZsW9-Ty7PJxO7iJViLzDD_mGG7ns/view?usp=sharing)
- Roboflow: [View or download the dataset](https://universe.roboflow.com/sown/pen-pfrzk)

## Dataset Format

The dataset is expected to use the YOLO object-detection format:

```text
dataset/
├── train/
│   ├── images/
│   └── labels/
├── val/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/
```

## Setup

1. Download the dataset ZIP from Google Drive or Roboflow.
2. Extract its contents into this `dataset/` directory.
3. Make sure the `train`, `val`, and `test` folders contain both `images/` and `labels/` subfolders.
4. Run `real-time-pen-pencil-detector.ipynb` in Google Colab.

## Dataset Notes

- The project uses a labeled dataset for custom pen/pencil object detection.
- The training notebook checks labels and prepares a single-class YOLO dataset.
- Keep the original dataset license and attribution information when using or sharing the data.
