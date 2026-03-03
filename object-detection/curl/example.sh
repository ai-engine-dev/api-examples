#!/bin/bash
# Object Detection API — cURL example
# Docs: https://ai-engine.net/apis/object-detection

curl -X POST \
  'https://objects-detection.p.rapidapi.com/objects-detection' \
  -H 'x-rapidapi-host: objects-detection.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=https://raw.githubusercontent.com/ai-engine-dev/api-examples/master/assets/samples/street.jpg'
