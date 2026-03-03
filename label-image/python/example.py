#!/usr/bin/env python3
"""Label Image API — Python example.

Docs: https://ai-engine.net/apis/label-image
"""

import requests

HOST = "label-image.p.rapidapi.com"
URL = f"https://{HOST}/detect-label"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": "YOUR_API_KEY",
}

payload = {"url": "https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/street.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
for label in data["body"]["labels"]:
    print(f"  {label['description']}: {label['score']:.3f}")
