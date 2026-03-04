#!/bin/bash
# Label Image API — cURL example
# Docs: https://ai-engine.net/apis/label-image

curl -X POST \
  'https://label-image.p.rapidapi.com/detect-label' \
  -H 'x-rapidapi-host: label-image.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=https://openmediadata.s3.eu-west-3.amazonaws.com/birds.jpeg'
