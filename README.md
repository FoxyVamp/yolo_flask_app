---
title: YOLOv8 Phone and Laptop Detection
emoji: 🚀
colorFrom: purple
colorTo: blue
sdk: docker
app_port: 7860
---

# 📱💻 Phone vs Laptop Detection App

## Project Overview
This project is an end-to-end machine learning application that detects **phones and laptops** in images using a **YOLOv8 object detection model**.

The system allows users to upload an image through a web interface and receive predictions with bounding boxes and confidence scores.

---

# 1. What the Model Does
The model performs **object detection**, identifying and localizing objects within an image.

- **Model:** YOLOv8 (Ultralytics)
- **Classes:** phone, laptop
- **Task:** Detect objects + draw bounding boxes
- **Output:** Image with bounding boxes + confidence score

The model was trained on a custom dataset and optimized to improve detection of smaller objects such as phones.

---

## ✨ Features
- Upload an image through a web interface
- Detect phones and laptops
- Display bounding boxes with confidence scores
- Clean and user-friendly UI
- Fully deployed as a web application

---

## 🖼️ Preview of the Application
![App Preview](https://github.com/user-attachments/assets/910ff2b7-d885-4284-94d6-e2a0b8500cb1)

---

## 🌐 Live Demo
👉 https://huggingface.co/spaces/FoxyVamp/yolo-phone-laptop-detection

---

# 🐳 2. Run Locally with Docker

### Step 1: Clone the repository
```bash
git clone https://github.com/FoxyVamp/yolo_flask_app.git
cd yolo_flask_app
```
### Step 2: Build Docker image
```bash
docker build -t yolo-app .
```
### Step 3: Run container
```bash
docker run -p 7860:7860 yolo-app
```
### Step 4: Open in browser
```bash
http://localhost:7860
```

# ❓ 3. How to Use the Interface
1. Open the application in your browser
2. Upload an image
3. Click Run Detection
4. The model will process the image
5. View the result with bounding boxes and confidence scores

# ⚠️ 4. Known Issues & Limitations
- The model only detects two classes: phone and laptop
- Detection performance depends on:
  - image quality
  - lighting conditions
  - object size and angle
- Smaller objects (like phones) may be harder to detect at lower resolutions
- Running on CPU may result in slower inference
- The **first request** may be **slower** due to **cold** start on free hosting

# ⚙️ 5. Technical Details
- Backend: Flask
- Model Framework: Ultralytics YOLOv8
- Deployment: Docker + Hugging Face Spaces
- Server: Gunicorn (production-ready)


# Conclusion

This project demonstrates a complete machine learning workflow:

1. Model training and optimization
2. Building a web interface
3. Docker containerization
4. Cloud deployment

It highlights the trade-off between accuracy and performance, especially when handling small objects in CPU-based environments.
