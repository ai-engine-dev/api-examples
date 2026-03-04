#!/usr/bin/env python3
"""NSFW Detect API — Python example.

Docs: https://ai-engine.net/apis/nsfw-detect
"""

import os
import requests

HOST = "nsfw-detect3.p.rapidapi.com"
URL = f"https://{HOST}/nsfw-detect"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "YOUR_API_KEY"),
}

payload = {"url": "https://openmediadata.s3.eu-west-3.amazonaws.com/violence.jpeg"}

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
