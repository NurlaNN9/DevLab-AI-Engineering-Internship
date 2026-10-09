from pathlib import Path
import time

import cv2
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "models" / "best.pt"
CONFIDENCE_THRESHOLD = 0.35
IMAGE_SIZE = 640
CAMERA_INDEX = 0


def main():
    global CONFIDENCE_THRESHOLD
    if not MODEL_PATH.is_file():
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}. "
            "Place your trained best.pt in the models folder."
        )

    model = YOLO(str(MODEL_PATH))
    camera = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)
    if not camera.isOpened():
        camera.release()
        camera = cv2.VideoCapture(CAMERA_INDEX)
    if not camera.isOpened():
        raise RuntimeError(
            "Could not open the webcam. Close apps using it or change CAMERA_INDEX."
        )

    fps = 0.0
    previous_time = time.perf_counter()
    print("Press Q to quit; +/= raises and - lowers the confidence threshold.")

    try:
        while True:
            success, frame = camera.read()
            if not success:
                print("Could not read a frame from the webcam.")
                break

            result = model.predict(
                source=frame,
                conf=CONFIDENCE_THRESHOLD,
                imgsz=IMAGE_SIZE,
                device="cpu",
                verbose=False,
            )[0]

            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                confidence = float(box.conf[0])
                class_id = int(box.cls[0])
                label = model.names.get(class_id, "object")
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    frame, f"{label} {confidence:.2f}",
                    (x1, max(25, y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 255, 0), 2,
                )

            current_time = time.perf_counter()
            frame_time = current_time - previous_time
            previous_time = current_time
            if frame_time > 0:
                measured_fps = 1.0 / frame_time
                fps = measured_fps if fps == 0 else 0.9 * fps + 0.1 * measured_fps

            cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
            cv2.putText(frame, f"Confidence threshold: {CONFIDENCE_THRESHOLD:.2f}",
                        (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 0, 0), 2)
            cv2.imshow("Pen/Pencil Detector", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            elif key in (ord("+"), ord("=")):
                CONFIDENCE_THRESHOLD = min(0.95, CONFIDENCE_THRESHOLD + 0.05)
            elif key == ord("-"):
                CONFIDENCE_THRESHOLD = max(0.05, CONFIDENCE_THRESHOLD - 0.05)
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
