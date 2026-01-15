import boto3
import os
import json
from time import sleep

bucket_name = "video-intel-frames-emily" 
rek = boto3.client("rekognition")
s3 = boto3.client("s3")

frames_dir = "frames"
results = {}

for frame_file in sorted(os.listdir(frames_dir)):
    if not frame_file.endswith(".jpg"):
        continue
    
    frame_path = os.path.join(frames_dir, frame_file)
    
    print(f"Uploading {frame_file}...")
    s3.upload_file(frame_path, bucket_name, frame_file)
    
    print(f"Analyzing {frame_file}...")
    try:
        response = rek.detect_labels(
            Image={"S3Object": {"Bucket": bucket_name, "Name": frame_file}},
            MaxLabels=10,
            MinConfidence=70
        )
        results[frame_file] = response
    except Exception as e:
        print(f"Error analyzing {frame_file}: {e}")
    
    sleep(0.5)  

with open("rekognition_result.json", "w") as f:
    json.dump(results, f, indent=2)

print("Rekognition analysis done for all frames.")
