#!/usr/bin/env python3
"""Landmark Detection API — Python example.

Docs: https://ai-engine.net/apis/landmark-detection
"""

import requests

HOST = "landmarks-detection.p.rapidapi.com"
URL = f"https://{HOST}/detect-landmarks"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": "YOUR_API_KEY",
}

payload = {"url": "https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/landmark.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
for lm in data["body"]["landmarks"]:
    loc = lm["locations"][0] if lm["locations"] else {}
    print(f"  {lm['description']} ({lm['score']:.2f}) — {loc.get('latitude', '')}, {loc.get('longitude', '')}")
