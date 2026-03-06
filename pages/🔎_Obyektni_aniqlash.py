import streamlit as st
import cv2
import numpy as np
import time
from ultralytics import YOLO
from collections import Counter
import pandas as pd
import tempfile

from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import av


# =========================
# Modelni yuklash
# =========================
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()
names = model.names

st.set_page_config(
    page_title="Object Detection — Demo",
    page_icon="🎯",
    layout="wide"
)
st.logo(
    image="https://cdn-icons-png.flaticon.com/512/4712/4712035.png",
    # image='🤖',
    size='large'
)
st.title("Real vaqtda obyektni aniqlash")
st.markdown("Kamera / Rasm / Video rejimlaridan birini tanlang")

# st.set_page_config(page_title="Object Detection System", layout="wide")
# st.title("Real-time Object Detection System")
st.markdown("YOLOv8 asosida rasm, video va kamera orqali obyekt aniqlash tizimi")


# =========================
# Sidebar
# =========================
st.sidebar.header("⚙ Sozlamalar")

conf = st.sidebar.slider("Confidence Threshold", 0.1, 1.0, 0.4, 0.05)

selected_classes = st.sidebar.multiselect(
    "Tanlangan klasslar",
    list(names.values()),
    default=[]
)

mode = st.sidebar.selectbox(
    "Rejimni tanlang",
    ["Image", "Video", "Camera"]
)
if st.sidebar.button("← Bosh sahifaga qaytish"):
    st.switch_page("🏠_Home.py")


# =========================
# WebRTC Processor
# =========================

class ObjectDetectionProcessor:

    def __init__(self):

        self.model = model                # model
        self.conf = conf                  # sidebar
        self.selected_classes = selected_classes
        self.names = names

        self.counts = {}
        self.fps = 0.0

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        img = frame.to_ndarray(format="bgr24")

        start = time.time()
        results = self.model(img, conf=self.conf, verbose=False)
        end = time.time()

        class_list = []
        for box in results[0].boxes:
            cls_id = int(box.cls)
            cls_name = self.names.get(cls_id, "Unknown")
            if not self.selected_classes or cls_name in self.selected_classes:
                class_list.append(cls_name)

        self.counts = dict(Counter(class_list))
        self.fps = 1 / max(end - start, 0.001)
        self.counts = dict(Counter(class_list))
        self.fps = 1 / max(end - start, 0.001)


        annotated = results[0].plot()
        return av.VideoFrame.from_ndarray(annotated, format="bgr24")



# ───────────
# CAMERA MODE
# ───────────

if mode == "Camera":

    st.subheader("📷 Real-time Kamera")

    col1, col2 = st.columns([3, 1])

    with col1:
        webrtc_ctx = webrtc_streamer(
            key="object-detection",
            video_processor_factory=ObjectDetectionProcessor,
            rtc_configuration=RTCConfiguration(
                {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
            ),
            media_stream_constraints={
                "video": True,
                "audio": False,
            },
            async_processing=True)


    with col2:
        st.subheader("Live Statistika")

        placeholder_fps = st.empty()
        placeholder_chart = st.empty()
        placeholder_info = st.empty()

        if webrtc_ctx.video_processor:
            vp = webrtc_ctx.video_processor


            placeholder_fps.metric("FPS", f"{vp.fps:.2f}" if vp.fps > 0 else "—")


            if vp.counts and len(vp.counts) > 0:
                current_counts = vp.counts.copy()

                df = pd.DataFrame(
                    list(current_counts.items()),
                    columns=["Class", "Count"]
                ).sort_values("Count", ascending=False)

                placeholder_chart.dataframe(df, width='stretch')
                placeholder_chart.bar_chart(df.set_index("Class"), width='stretch')
            else:
                placeholder_info.info("Hozircha hech qanday obyekt aniqlanmadi yoki counts bo'sh")
        else:
            placeholder_info.info("Kamera protsessori hali tayyor emas")


    if webrtc_ctx.state is not None and webrtc_ctx.state.playing:
        time.sleep(0.7)
        st.rerun()
# =========================
# IMAGE MODE
# =========================
if mode == "Image":

    uploaded_file = st.file_uploader(
        "Rasm yuklang",
        type=["jpg","png","jpeg"]
    )

    if uploaded_file is not None:

        file_bytes = uploaded_file.read()

        image = cv2.imdecode(
            np.frombuffer(file_bytes,np.uint8),
            cv2.IMREAD_COLOR
        )

        start = time.time()

        results = model(image, conf=conf, verbose=False)

        end = time.time()

        class_list = []

        for box in results[0].boxes:

            cls_id = int(box.cls[0])
            cls_name = names[cls_id]

            if selected_classes and cls_name not in selected_classes:
                continue

            class_list.append(cls_name)

        counts = Counter(class_list)

        annotated = results[0].plot()

        st.image(
            annotated,
            channels="BGR",
            width="stretch"
        )

        st.subheader("Statistik natija")

        st.write("Ishlash vaqti:", round(end-start,3),"sekund")

        st.write("Jami obyekt:", sum(counts.values()))

        df = pd.DataFrame.from_dict(
            counts,
            orient="index",
            columns=["Count"]
        )

        st.bar_chart(df)

        _,buffer = cv2.imencode(".jpg", annotated)

        st.download_button(
            "Natijani yuklab olish",
            buffer.tobytes(),
            file_name="output.jpg"
        )


# =========================
# VIDEO MODE
# =========================
if mode == "Video":

    uploaded_video = st.file_uploader(
        "Video yuklang",
        type=["mp4","avi","mov"]
    )

    if uploaded_video is not None:

        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())

        cap = cv2.VideoCapture(tfile.name)

        stframe = st.empty()

        fps_placeholder = st.empty()

        counts_placeholder = st.empty()

        while cap.isOpened():

            ret, frame = cap.read()

            if not ret:
                break

            start = time.time()

            results = model(frame, conf=conf, verbose=False)

            end = time.time()

            class_list = []

            for box in results[0].boxes:

                cls_id = int(box.cls[0])
                cls_name = names[cls_id]

                if selected_classes and cls_name not in selected_classes:
                    continue

                class_list.append(cls_name)

            counts = Counter(class_list)

            annotated = results[0].plot()

            stframe.image(
                annotated,
                channels="BGR"
            )

            fps_placeholder.write(
                f"FPS: {round(1/max(end-start,0.001),2)}"
            )

            df = pd.DataFrame.from_dict(
                counts,
                orient="index",
                columns=["Count"]
            )
            counts_placeholder.bar_chart(
                df,
                horizontal=True,
                width='stretch'
            )


        cap.release()