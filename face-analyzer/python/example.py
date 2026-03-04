#!/usr/bin/env python3
"""Face Analyzer API — Python example.

Docs: https://ai-engine.net/apis/face-analyzer
"""

import os
import requests

HOST = "faceanalyzer-ai.p.rapidapi.com"
URL = f"https://{HOST}/faceanalysis"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "YOUR_API_KEY"),
}

payload = {"url": "https://openmediadata.s3.eu-west-3.amazonaws.com/face.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
for face in data["body"]["faces"]:
    features = face["facialFeatures"]
    age = features["AgeRange"]
    print(f"  Age: {age['Low']}-{age['High']}, Gender: {features['Gender']}")
