import os
import json
from datetime import timedelta

rek_file = "rekognition_result.json"
output_file = "output.json"

with open(rek_file) as f:
    rek_results = json.load(f)

merged = []

for frame_name, data in rek_results.items():
    # Extract frame number from filename
    frame_num = int(frame_name.split("_")[1].split(".")[0])
    
    # Assuming 30 FPS
    seconds = frame_num // 30
    timestamp = str(timedelta(seconds=seconds))
    
    entry = {
        "frame": frame_num,
        "timestamp": timestamp,
        "aws": {
            "labels": data.get("Labels", []),
            "faces": data.get("FaceDetails", []),
            "moderation": data.get("ModerationLabels", [])
        }
    }
    merged.append(entry)

with open(output_file, "w") as f:
    json.dump(merged, f, indent=2)

print(f"Merged results saved to {output_file}")
