#!/bin/bash
# Logo Detection API — cURL example
# Docs: https://ai-engine.net/apis/logo-detection

curl -X POST \
  'https://logos-detection.p.rapidapi.com/detect-logo' \
  -H 'x-rapidapi-host: logos-detection.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=https://openmediadata.s3.eu-west-3.amazonaws.com/pexels-macbook.jpg'
