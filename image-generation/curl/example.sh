#!/bin/bash
# Image Generation API — cURL example
# Docs: https://ai-engine.net/apis/image-generation

curl -X POST \
  'https://imagegenius-ai.p.rapidapi.com/generate-image' \
  -H 'x-rapidapi-host: imagegenius-ai.p.rapidapi.com' \
  -H 'x-rapidapi-key: YOUR_API_KEY' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'prompt=A futuristic city at sunset with flying cars'
