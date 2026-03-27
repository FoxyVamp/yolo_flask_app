# 📱💻 Phone vs Laptop Detection App

## Preview
<img width="1279" height="853" alt="image" src="https://github.com/user-attachments/assets/910ff2b7-d885-4284-94d6-e2a0b8500cb1" />

A Flask-based web application that uses a YOLOv8 deep learning model to detect phones and laptops from images.

## Model Overview
- Model: YOLOv8
- Classes: phone, laptop
- Framework: Flask
- Deployment: Docker

## Features
- Upload an image
- Detect phone or laptop
- Display result with bounding box and confidence

## Run Locally with Docker
```bash
Build the image:
docker build -t yolo-app .

Run the container:
docker run -p 5000:5000 yolo-app

Open in browser:
http://localhost:5000
```
## How to Use
1. Open the app in your browser
2. Upload an image
3. Click Run Detection
4. View the result

## Limitations
- Only detects phone and laptop
- Performance may vary depending on image quality
- Performance may vary depending on lighting, angle, and image quality
- This is a demo project and not optimized for production

 

The app is deployed on Render’s free tier, so the first request after inactivity may take longer because the service spins down when idle.


