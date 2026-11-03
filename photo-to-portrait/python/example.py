#!/usr/bin/env python3
"""Photo to Portrait API: Python example.

Docs: https://ai-engine.net/apis/photo-to-portrait
"""

import os
import requests

HOST = "phototoportrait.p.rapidapi.com"
URL = f"https://{HOST}/photo-to-portrait"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "YOUR_API_KEY"),
}

payload = {"url": "https://openmediadata.s3.eu-west-3.amazonaws.com/face.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
print(f"Result: {data['image_url']}")
print(f"Size: {data['width']}x{data['height']}")
