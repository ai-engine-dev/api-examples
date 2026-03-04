#!/usr/bin/env python3
"""Face Restoration API — Python example.

Docs: https://ai-engine.net/apis/face-restoration
"""

import os
import requests

HOST = "face-restoration.p.rapidapi.com"
URL = f"https://{HOST}/submit"

headers = {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "YOUR_API_KEY"),
}

payload = {"image_url": "https://openmediadata.s3.eu-west-3.amazonaws.com/face_restoration_api_demo_source.jpg"}

response = requests.post(
    URL,
    headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

data = response.json()
job_id = data["jobId"]
print(f"Job submitted: {job_id}")
print("Poll GET /result?jobId={job_id} until status is done")
