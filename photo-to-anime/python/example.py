#!/usr/bin/env python3
"""Photo to Anime API — Python example.

Docs: https://ai-engine.net/apis/photo-to-anime
"""

import os
import requests

HOST = "phototoanime1.p.rapidapi.com"
URL = f"https://{HOST}/cartoonize"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "YOUR_API_KEY"),
}

payload = {"image_url": "https://raw.githubusercontent.com/ai-engine-dev/api-examples/master/assets/samples/face.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
print(f"Result: {data['image_url']}")
print(f"Size: {data['width']}x{data['height']}")
