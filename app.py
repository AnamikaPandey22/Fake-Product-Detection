import streamlit as st
from ultralytics import YOLO
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2

# Load models
yolo_model = YOLO("best.pt")
resnet_model = load_model("Logo_classifier_image.keras")

st.title("🧠 Fake Product Logo Detector")
uploaded_file = st.file_uploader("Upload a product image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Save uploaded image
    with open("input.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image("input.jpg", caption="Uploaded Image", use_container_width=True)

    # YOLO detection
    results = yolo_model.predict("input.jpg", save=False)

    for r in results:
        im = r.orig_img.copy()
        boxes = r.boxes.xyxy.cpu().numpy()

        if len(boxes) > 0:
            # Crop first detected logo
            x1, y1, x2, y2 = boxes[0].astype(int)
            cropped = im[y1:y2, x1:x2]
            cv2.imwrite("cropped.jpg", cropped)

            st.image("cropped.jpg", caption="Detected Logo", width=250)

            # ResNet classification
            img = image.load_img("cropped.jpg", target_size=(128, 128))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            pred = resnet_model.predict(img_array)
            label = "REAL ✅" if np.argmax(pred) == 1 else "FAKE ❌"

            st.success(f"Prediction: {label}")
        else:
            st.warning("⚠️ No logo detected in the image.")


