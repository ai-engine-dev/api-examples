#!/bin/bash
# Photo to Anime API — cURL example
# Docs: https://ai-engine.net/apis/photo-to-anime

curl -X POST \
  'https://phototoanime1.p.rapidapi.com/cartoonize' \
  -H 'x-rapidapi-host: phototoanime1.p.rapidapi.com' \
  -H 'x-rapidapi-key: YOUR_API_KEY' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'image_url=https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/face.jpg'
