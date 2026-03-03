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

payload = {"url": "https://raw.githubusercontent.com/ai-engine-dev/api-examples/master/assets/samples/face.jpg"}

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
