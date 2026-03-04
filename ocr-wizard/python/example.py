#!/usr/bin/env python3
"""OCR Wizard API — Python example.

Docs: https://ai-engine.net/apis/ocr-wizard
"""

import os
import requests

HOST = "ocr-wizard.p.rapidapi.com"
URL = f"https://{HOST}/ocr"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "YOUR_API_KEY"),
}

payload = {"url": "https://openmediadata.s3.eu-west-3.amazonaws.com/pexels-monstera-5709059.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
print(f"Language: {data['body']['detectedLanguage']}")
print(f"Text: {data['body']['fullText']}")
