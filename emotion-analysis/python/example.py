#!/usr/bin/env python3
"""Emotion & Personality Analysis API — Python example.

Docs: https://ai-engine.net/apis/emotion-analysis
"""

import requests

HOST = "emotion-sentiment-personality-analysis.p.rapidapi.com"
URL = f"https://{HOST}/emotions"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": "YOUR_API_KEY",
}

payload = {"text": "I am so happy today! The weather is beautiful and I feel great."}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
for emotion in data["emotions"]:
    print(f"  {emotion['label']}: {emotion['score']:.3f}")
