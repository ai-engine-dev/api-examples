#!/bin/bash
# Photo to Anime API — cURL example
# Docs: https://ai-engine.net/apis/photo-to-anime

curl -X POST \
  'https://phototoanime1.p.rapidapi.com/cartoonize' \
  -H 'x-rapidapi-host: phototoanime1.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'image_url=https://openmediadata.s3.eu-west-3.amazonaws.com/face.jpg'
