# 🖥️ Intelligent Video Processing Pipeline

An intelligent video processing pipeline for automated visual content analysis using **AWS Rekognition** and **GCP Vision**. The system supports both **pre-recorded videos** and **real-time webcam input**, extracting frames, detecting objects/scenes, and generating both **annotated visuals** and **structured JSON outputs**.

---

## 📘 About This Project

This project allows flexible video analysis across multiple use cases. Video frames are extracted at configurable intervals, uploaded to **Amazon S3**, and analyzed using **AWS Rekognition** to detect objects, scenes, and visual labels with confidence scores. 

- For offline video: labels are overlaid on extracted frames  
- For live webcam: detections appear in real-time with annotations  

The modular design ensures scalability, cost-efficiency, and easy integration with downstream applications such as surveillance, content moderation, and smart monitoring.

---

## 🔍 Features

- 🧠 Automatic object and scene detection using AWS Rekognition  
- 🎯 Support for offline video and live webcam input  
- ⬛ Annotated visual output for easy interpretation  
- 📄 Structured JSON outputs for analytics or downstream processing  
- 🌐 Modular, scalable, and cloud-integrated  

---

## 🛠️ Tech Stack

- **Programming Language:** Python 3.8+  
- **Computer Vision:** OpenCV  
- **Cloud Services:** AWS Rekognition, AWS S3  
- **Data Handling:** JSON, os, datetime  
- **Optional:** GCP Vision API integration  

---

## 🧰 Installation & Usage

### 🔧 Setup Environment

1. **Clone the repository:**

git clone https://github.com/Ilakiya-Emily05/INTUERA.git
cd INTUERA
(Optional) Create a virtual environment:


conda create -n video-pipeline python=3.9
conda activate video-pipeline
Install dependencies:


pip install -r requirements.txt
Run the pipeline:


python main.py
Enter 1 for video file analysis

Enter 2 for live webcam analysis

⚙️ Workflow
🎥 Video Analysis Mode
Reads a video file from a local path

Extracts frames at a configurable interval

Uploads frames to S3

Uses AWS Rekognition to detect objects and scenes

Saves annotated frames and structured JSON results

🖥️ Webcam Mode
Captures frames from a live webcam

Uploads selected frames periodically to AWS Rekognition

Displays real-time label overlays on the live feed

Stores annotated frames and JSON results

📊 Performance Analysis
High detection accuracy using AWS Rekognition

Optimized frame extraction reduces processing time and API calls

Real-time webcam mode maintains low latency

JSON outputs and visual annotations provide dual interpretability

✅ Advantages
No need for local ML model training

Supports offline and live analysis

Cloud-powered scalability

Clear visual annotations for human-friendly interpretation

Structured JSON for integration with dashboards or analytics tools

🌐 Applications
Security & Surveillance: Detect objects/activities in real-time or recorded footage

Smart Cities: Traffic monitoring, public space analysis

Retail Analytics: Customer behavior and scene context analysis

Research & Education: Demonstration of cloud-based video analytics

Media Monitoring: Content moderation and event detection

🧾 System Requirements
Hardware
PC or laptop with 8 GB RAM, multi-core processor

Webcam for live mode

Stable internet connection

Software
Python 3.8+

OpenCV, Boto3, and standard Python libraries

Cloud
AWS Account with access to Rekognition and S3

Proper IAM permissions configured

📌 Future Improvements
Add face recognition and emotion detection

Integrate real-time dashboards

Extend to multi-camera setups

Optional GCP Vision integration

