#!/bin/bash
# Photo to Portrait API: cURL example
# Docs: https://ai-engine.net/apis/photo-to-portrait

curl -X POST \
  'https://phototoportrait.p.rapidapi.com/photo-to-portrait' \
  -H 'x-rapidapi-host: phototoportrait.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=https://openmediadata.s3.eu-west-3.amazonaws.com/face.jpg'
