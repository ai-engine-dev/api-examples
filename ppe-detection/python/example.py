#!/usr/bin/env python3
"""PPE Detection API — Python example.

Docs: https://ai-engine.net/apis/ppe-detection
"""

import os
import requests

HOST = "ppe-detection1.p.rapidapi.com"
URL = f"https://{HOST}/detect-ppe"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "YOUR_API_KEY"),
}

payload = {"url": "https://openmediadata.s3.eu-west-3.amazonaws.com/pexels-antoni-shkraba-5493662.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
for person in data["body"]["Persons"]:
    print(f"  Head: {person['HeadCover']}, Face: {person['FaceCover']}")
