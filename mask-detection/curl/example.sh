#!/bin/bash
# Mask Detection API — cURL example
# Docs: https://ai-engine.net/apis/mask-detection

curl -X POST \
  'https://mask-detection2.p.rapidapi.com/detect-mask' \
  -H 'x-rapidapi-host: mask-detection2.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=https://openmediadata.s3.eu-west-3.amazonaws.com/pexels-cottonbro-studio-3957986.jpg'
