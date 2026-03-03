#!/usr/bin/env python3
"""Mask Detection API — Python example.

Docs: https://ai-engine.net/apis/mask-detection
"""

import os
import requests

HOST = "mask-detection2.p.rapidapi.com"
URL = f"https://{HOST}/detect-mask"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "YOUR_API_KEY"),
}

payload = {"url": "https://raw.githubusercontent.com/ai-engine-dev/api-examples/master/assets/samples/face.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
summary = data["body"]["Summary"]
print(f"With mask: {summary['PersonsWithMask']}")
print(f"Without mask: {summary['PersonsWithoutMask']}")
