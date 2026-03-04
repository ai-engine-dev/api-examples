#!/bin/bash
# PPE Detection API — cURL example
# Docs: https://ai-engine.net/apis/ppe-detection

curl -X POST \
  'https://ppe-detection1.p.rapidapi.com/detect-ppe' \
  -H 'x-rapidapi-host: ppe-detection1.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=https://openmediadata.s3.eu-west-3.amazonaws.com/pexels-antoni-shkraba-5493662.jpg'
