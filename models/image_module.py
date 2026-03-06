import cv2
import time
from ultralytics import YOLO
from collections import Counter

def detect_image(image_path, conf=0.25):

    model = YOLO("../yolov8n.pt")

    image = cv2.imread(image_path)

    start_time = time.time()
    results = model(image, conf=conf, verbose=False)
    end_time = time.time()

    boxes = results[0].boxes
    names = model.names

    class_list = []

    for box in boxes:
        cls_id = int(box.cls[0])
        class_name = names[cls_id]
        class_list.append(class_name)

    counts = Counter(class_list)

    annotated_image = results[0].plot()

    processing_time = end_time - start_time

    print("Ishlash vaqti:", round(processing_time, 3), "sekund")
    print("Jami obyektlar:", sum(counts.values()))

    for cls, count in counts.items():
        print(f"{cls}: {count}")

    cv2.imshow("Image Detection", annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()