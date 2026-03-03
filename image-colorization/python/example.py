#!/usr/bin/env python3
"""Image Colorization API — Python example.

Docs: https://ai-engine.net/apis/image-colorization
"""

import requests

HOST = "photocolorizer-ai.p.rapidapi.com"
URL = f"https://{HOST}/colorize-photo"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": "YOUR_API_KEY",
}

payload = {"url": "https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/bw-portrait.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
print(f"Colorized image: {data['body']['imageUrl']}")
