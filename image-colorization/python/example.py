#!/usr/bin/env python3
"""Image Colorization API — Python example.

Docs: https://ai-engine.net/apis/image-colorization
"""

import os
import requests

HOST = "photocolorizer-ai.p.rapidapi.com"
URL = f"https://{HOST}/colorize-photo"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "YOUR_API_KEY"),
}

payload = {"url": "https://openmediadata.s3.eu-west-3.amazonaws.com/pexels-suzy-hazelwood-5292049.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
print(f"Colorized image: {data['body']['imageUrl']}")
