#!/bin/bash
# Logo Detection API — cURL example
# Docs: https://ai-engine.net/apis/logo-detection

curl -X POST \
  'https://logos-detection.p.rapidapi.com/detect-logo' \
  -H 'x-rapidapi-host: logos-detection.p.rapidapi.com' \
  -H 'x-rapidapi-key: YOUR_API_KEY' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/street.jpg'
