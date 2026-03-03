#!/usr/bin/env python3
"""Image Generation API — Python example.

Docs: https://ai-engine.net/apis/image-generation
"""

import os
import requests

HOST = "imagegenius-ai.p.rapidapi.com"
URL = f"https://{HOST}/generate-image"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "YOUR_API_KEY"),
}

payload = {"prompt": "A futuristic city at sunset with flying cars"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
print(f"Generated image: {data['body']['imageUrl']}")
