#!/usr/bin/env python3
"""Logo Detection API — Python example.

Docs: https://ai-engine.net/apis/logo-detection
"""

import os
import requests

HOST = "logos-detection.p.rapidapi.com"
URL = f"https://{HOST}/detect-logo"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "YOUR_API_KEY"),
}

payload = {"url": "https://raw.githubusercontent.com/ai-engine-dev/api-examples/master/assets/samples/street.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
for logo in data["body"]["logos"]:
    print(f"  {logo['description']}: {logo['score']:.3f}")
