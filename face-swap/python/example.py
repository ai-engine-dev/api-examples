#!/usr/bin/env python3
"""Face Swap API — Python example.

Docs: https://ai-engine.net/apis/face-swap
"""

import os
import requests

HOST = "deepfake-face-swap-ai.p.rapidapi.com"
URL = f"https://{HOST}/swap-face"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "YOUR_API_KEY"),
}

payload = {"source_url": "https://openmediadata.s3.eu-west-3.amazonaws.com/faceswap_api_demo_source.jpg", "target_url": "https://openmediadata.s3.eu-west-3.amazonaws.com/faceswap_api_demo_group.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
print(f"Result: {data['image_url']}")
print(f"Size: {data['width']}x{data['height']}")
