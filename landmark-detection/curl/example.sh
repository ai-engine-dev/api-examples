#!/bin/bash
# Landmark Detection API — cURL example
# Docs: https://ai-engine.net/apis/landmark-detection

curl -X POST \
  'https://landmarks-detection.p.rapidapi.com/detect-landmarks' \
  -H 'x-rapidapi-host: landmarks-detection.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=https://raw.githubusercontent.com/ai-engine-dev/api-examples/master/assets/samples/landmark.jpg'
