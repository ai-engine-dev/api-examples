#!/usr/bin/env python3
"""OCR Wizard API — Python example.

Docs: https://ai-engine.net/apis/ocr-wizard
"""

import requests

HOST = "ocr-wizard.p.rapidapi.com"
URL = f"https://{HOST}/ocr"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": "YOUR_API_KEY",
}

payload = {"url": "https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/text.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
print(f"Language: {data['body']['detectedLanguage']}")
print(f"Text: {data['body']['fullText']}")
