#!/usr/bin/env python3
"""Face Analyzer API — Python example.

Docs: https://ai-engine.net/apis/face-analyzer
"""

import requests

HOST = "faceanalyzer-ai.p.rapidapi.com"
URL = f"https://{HOST}/faceanalysis"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": "YOUR_API_KEY",
}

payload = {"url": "https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/face.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
for face in data["body"]["faces"]:
    print(f"  Age: {face['AgeRange']}, Gender: {face['Gender']}")
