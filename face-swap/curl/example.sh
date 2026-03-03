#!/bin/bash
# Face Swap API — cURL example
# Docs: https://ai-engine.net/apis/face-swap

curl -X POST \
  'https://deepfake-face-swap-ai.p.rapidapi.com/swap-face' \
  -H 'x-rapidapi-host: deepfake-face-swap-ai.p.rapidapi.com' \
  -H 'x-rapidapi-key: YOUR_API_KEY' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'source_url=https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/face.jpg&target_url=https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/face2.jpg'
