#!/usr/bin/env python3
"""PPE Detection API — Python example.

Docs: https://ai-engine.net/apis/ppe-detection
"""

import requests

HOST = "ppe-detection1.p.rapidapi.com"
URL = f"https://{HOST}/detect-ppe"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": "YOUR_API_KEY",
}

payload = {"url": "https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/construction.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
for person in data["body"]["Persons"]:
    print(f"  Head: {person['HeadCover']}, Face: {person['FaceCover']}")
