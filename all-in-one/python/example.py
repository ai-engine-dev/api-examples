#!/usr/bin/env python3
"""AI All-in-One API: Python example.

One key for OCR, face analysis, background removal, text analysis and more.
Docs: https://ai-engine.net/apis/all-in-one
"""

import os
import requests

HOST = "ai-all-in-one.p.rapidapi.com"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "YOUR_API_KEY"),
    "Content-Type": "application/x-www-form-urlencoded",
}

# Extract text from an image
ocr = requests.post(
    f"https://{HOST}/v1/ocr",
    headers=headers,
    data={"url": "https://openmediadata.s3.eu-west-3.amazonaws.com/pexels-monstera-5709059.jpg"},
).json()
print(f"Text: {ocr['body']['fullText']}")

# Same key, another endpoint: sentiment of a review
sentiment = requests.post(
    f"https://{HOST}/v1/sentiment",
    headers=headers,
    data={"text": "I love this product, it works great"},
).json()
print(f"Sentiment: {sentiment['sentiment']['label']} ({sentiment['sentiment']['score']})")
