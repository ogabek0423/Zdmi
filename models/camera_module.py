import cv2
import time
from ultralytics import YOLO
from collections import Counter

def run_camera():

    model = YOLO("../yolov8n.pt")  # eng tez model

    cap = cv2.VideoCapture(0)  # 0 = laptop kamera

    if not cap.isOpened():
        print("Kamera ochilmadi!")
        return

    print("Kamera ishga tushdi... Chiqish uchun 'q' bosing")

    while True:
        start_time = time.time()

        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, verbose=False)
        boxes = results[0].boxes
        names = model.names

        class_list = []

        for box in boxes:
            cls_id = int(box.cls[0])
            class_name = names[cls_id]
            class_list.append(class_name)

        counts = Counter(class_list)

        # Natijani chizish
        annotated_frame = results[0].plot()

        # FPS hisoblash
        end_time = time.time()
        fps = 1 / (end_time - start_time)

        # FPS ni chiqarish
        cv2.putText(
            annotated_frame,
            f"FPS: {int(fps)}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        # Klass statistikasini chiqarish
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

        cv2.imshow("Real-time Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()