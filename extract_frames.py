import cv2
import os

video_path = r"C:\Users\ilaki\OneDrive\Desktop\Intuera\video-intelligence\input\input.mp4"
output_dir = "frames"

os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video")
    exit()

count = 0
saved = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if count % 30 == 0:
        frame_path = os.path.join(output_dir, f"frame_{count}.jpg")
        cv2.imwrite(frame_path, frame)
        saved += 1

    count += 1

cap.release()
print(f"Saved {saved} frames")
