import cv2
import os
import boto3
import json
import time
from datetime import timedelta


video_path = "YOUR_LOCAL_VIDEO_PATH/input.mp4"
bucket_name = "YOUR_BUCKET_NAME"

fps_extract = 30               
WEBCAM_INTERVAL = 2             

frames_dir_vid = "frames_video"
frames_dir_webcam = "frames_webcam"

annot_vid = "frames_annotated_video"
annot_webcam = "frames_annotated_webcam"

json_vid = "output_video.json"
json_webcam = "output_webcam.json"


rek = boto3.client("rekognition")
s3 = boto3.client("s3")

print("\nSelect input source:")
print("1. Video file")
print("2. Webcam live\n")
choice = input("Enter 1 or 2: ").strip()

if choice == "1":

    os.makedirs(frames_dir_vid, exist_ok=True)
    os.makedirs(annot_vid, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Could not open video.")
        exit()

    count = 0
    saved = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if count % fps_extract == 0:
            name = f"frame_{count}.jpg"
            path = os.path.join(frames_dir_vid, name)
            cv2.imwrite(path, frame)
            saved.append(name)

        count += 1

    cap.release()
    print(f"Extracted {len(saved)} frames.")

    results = []

    for fname in saved:
        fpath = os.path.join(frames_dir_vid, fname)
        s3.upload_file(fpath, bucket_name, fname)

        response = rek.detect_labels(
            Image={"S3Object": {"Bucket": bucket_name, "Name": fname}},
            MaxLabels=10,
            MinConfidence=70
        )

        frame = cv2.imread(fpath)
        h, w, _ = frame.shape

        y = 50
        for lbl in response["Labels"]:
            text = f"{lbl['Name']} ({int(lbl['Confidence'])}%)"
            cv2.putText(frame, text, (10, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.4,
                        (255,255,255), 6)
            cv2.putText(frame, text, (10, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.4,
                        (0,0,0), 3)
            y += 55

            for inst in lbl.get("Instances", []):
                box = inst["BoundingBox"]
                x1 = int(box["Left"] * w)
                y1 = int(box["Top"] * h)
                x2 = int((box["Left"] + box["Width"]) * w)
                y2 = int((box["Top"] + box["Height"]) * h)
                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,0,0), 3)

        cv2.imwrite(os.path.join(annot_vid, fname), frame)

        frame_num = int(fname.split("_")[1].split(".")[0])
        results.append({
            "frame": frame_num,
            "timestamp": str(timedelta(seconds=frame_num // fps_extract)),
            "labels": response["Labels"]
        })

        time.sleep(0.4)

    with open(json_vid, "w") as f:
        json.dump(results, f, indent=2)

    print("Video pipeline complete.")


elif choice == "2":

    os.makedirs(frames_dir_webcam, exist_ok=True)
    os.makedirs(annot_webcam, exist_ok=True)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam.")
        exit()

    print("Live webcam running. Press Q to quit.")

    last_call = 0
    frame_id = 0
    data = []

    response_labels = {}
    response_faces = {}

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        now = time.time()

        if now - last_call >= WEBCAM_INTERVAL:
            _, enc = cv2.imencode(".jpg", frame)
            img_bytes = enc.tobytes()

            response_labels = rek.detect_labels(
                Image={"Bytes": img_bytes},
                MaxLabels=6,
                MinConfidence=70
            )

            response_faces = rek.detect_faces(
                Image={"Bytes": img_bytes},
                Attributes=["ALL"]
            )

            last_call = now

        h, w, _ = frame.shape

        # ===== LABELS =====
        y = 40
        for lbl in response_labels.get("Labels", []):
            text = f"{lbl['Name']} ({int(lbl['Confidence'])}%)"
            cv2.putText(frame, text, (10, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2,
                        (255,255,255), 5)
            cv2.putText(frame, text, (10, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2,
                        (0,0,0), 3)
            y += 45

            for inst in lbl.get("Instances", []):
                box = inst["BoundingBox"]
                x1 = int(box["Left"] * w)
                y1 = int(box["Top"] * h)
                x2 = int((box["Left"] + box["Width"]) * w)
                y2 = int((box["Top"] + box["Height"]) * h)
                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,0,0), 3)

        for face in response_faces.get("FaceDetails", []):
            box = face["BoundingBox"]
            x1 = int(box["Left"] * w)
            y1 = int(box["Top"] * h)
            x2 = int((box["Left"] + box["Width"]) * w)
            y2 = int((box["Top"] + box["Height"]) * h)

            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,0,255), 3)

            emotions = sorted(
                face.get("Emotions", []),
                key=lambda e: e["Confidence"],
                reverse=True
            )

            if emotions:
                mood = emotions[0]["Type"]
                conf = int(emotions[0]["Confidence"])
                cv2.putText(frame, f"{mood} ({conf}%)",
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1.0, (0,0,255), 3)

        cv2.imshow("Live Webcam Detection", frame)

        cv2.imwrite(os.path.join(annot_webcam, f"webcam_{frame_id}.jpg"), frame)

        data.append({
            "frame": frame_id,
            "labels": response_labels.get("Labels", []),
            "faces": response_faces.get("FaceDetails", [])
        })

        frame_id += 1

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    with open(json_webcam, "w") as f:
        json.dump(data, f, indent=2)

    print("Webcam pipeline complete.")

else:
    print("Invalid choice.")
