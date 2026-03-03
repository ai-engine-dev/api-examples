#!/usr/bin/env python3
"""NSFW Detect API — Python example.

Docs: https://ai-engine.net/apis/nsfw-detect
"""

import requests

HOST = "nsfw-detect3.p.rapidapi.com"
URL = f"https://{HOST}/nsfw-detect"

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
labels = data["body"]["ModerationLabels"]
if labels:
    for l in labels:
        print(f"  {l['Name']}: {l['Confidence']:.1f}%")
else:
    print("  Image is safe")
