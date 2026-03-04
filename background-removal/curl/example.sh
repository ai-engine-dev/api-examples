#!/bin/bash
# Background Removal API — cURL example
# Docs: https://ai-engine.net/apis/background-removal

curl -X POST \
  'https://background-removal-ai.p.rapidapi.com/remove-background' \
  -H 'x-rapidapi-host: background-removal-ai.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"image_url": "https://openmediadata.s3.eu-west-3.amazonaws.com/face.jpg"}'
