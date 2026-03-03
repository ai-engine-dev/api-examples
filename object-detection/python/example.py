#!/usr/bin/env python3
"""Object Detection API — Python example.

Docs: https://ai-engine.net/apis/object-detection
"""

import os
import requests

HOST = "objects-detection.p.rapidapi.com"
URL = f"https://{HOST}/objects-detection"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "YOUR_API_KEY"),
}

payload = {"url": "https://raw.githubusercontent.com/ai-engine-dev/api-examples/master/assets/samples/street.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
for obj in data["body"]["labels"]:
    print(f"  {obj['Name']}: {obj['Confidence']:.1f}%")
