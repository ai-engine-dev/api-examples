#!/usr/bin/env python3
"""Background Removal API — Python example.

Docs: https://ai-engine.net/apis/background-removal
"""

import requests

HOST = "background-removal-ai.p.rapidapi.com"
URL = f"https://{HOST}/remove-background"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": "YOUR_API_KEY",
}

payload = {"image_url": "https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/object.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/json"},
    json=payload,
)

data = response.json()
print(f"Result: {data['image_url']}")
print(f"Size: {data['width']}x{data['height']}")
