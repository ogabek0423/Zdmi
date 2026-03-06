import cv2
import time
from ultralytics import YOLO
from collections import Counter

def detect_video(video_path, conf=0.25):

    model = YOLO("../yolov8n.pt")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Video ochilmadi!")
        return

    print("Video boshlandi... Chiqish uchun 'q' bosing")

    while True:
        start_time = time.time()

        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, conf=conf, verbose=False)
        boxes = results[0].boxes
        names = model.names

        class_list = []

        for box in boxes:
            cls_id = int(box.cls[0])
            class_name = names[cls_id]
            class_list.append(class_name)

        counts = Counter(class_list)

        annotated_frame = results[0].plot()

        end_time = time.time()
        fps = 1 / (end_time - start_time)

        cv2.putText(
            annotated_frame,
            f"FPS: {int(fps)}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        y_offset = 80
        for cls, count in counts.items():
            text = f"{cls}: {count}"
            cv2.putText(
                annotated_frame,
                text,
                (20, y_offset),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 0, 0),
                2
            )
            y_offset += 30

        cv2.imshow("Video Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()