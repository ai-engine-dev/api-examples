#!/usr/bin/env python3
"""Label Image API — Python example.

Docs: https://ai-engine.net/apis/label-image
"""

import os
import requests

HOST = "label-image.p.rapidapi.com"
URL = f"https://{HOST}/detect-label"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "YOUR_API_KEY"),
}

payload = {"url": "https://openmediadata.s3.eu-west-3.amazonaws.com/birds.jpeg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
for label in data["body"]["labels"]:
    print(f"  {label['description']}: {label['score']:.3f}")
