#!/bin/bash
# Face Restoration API — cURL example
# Docs: https://ai-engine.net/apis/face-restoration

curl -X POST \
  'https://face-restoration.p.rapidapi.com/submit' \
  -H 'x-rapidapi-host: face-restoration.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'image_url=https://openmediadata.s3.eu-west-3.amazonaws.com/face_restoration_api_demo_source.jpg'
