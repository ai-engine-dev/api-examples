#!/usr/bin/env python3
"""Face Restoration API: Python example.

Docs: https://ai-engine.net/apis/face-restoration
"""

import os
import requests

HOST = "face-restoration.p.rapidapi.com"
URL = f"https://{HOST}/enhance-face"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "YOUR_API_KEY"),
}

payload = {"image_url": "https://openmediadata.s3.eu-west-3.amazonaws.com/face_restoration_api_demo_source.jpg", "mode": "single"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
print(f"Result: {data['image_url']}")
print(f"Faces restored: {data['faces_detected']}")
