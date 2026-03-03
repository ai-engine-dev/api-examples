#!/usr/bin/env python3
"""Face Swap API — Python example.

Docs: https://ai-engine.net/apis/face-swap
"""

import requests

HOST = "deepfake-face-swap-ai.p.rapidapi.com"
URL = f"https://{HOST}/swap-face"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": "YOUR_API_KEY",
}

payload = {"source_url": "https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/face.jpg", "target_url": "https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/face2.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
print(f"Result: {data['image_url']}")
print(f"Size: {data['width']}x{data['height']}")
