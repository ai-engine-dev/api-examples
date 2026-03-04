#!/bin/bash
# Face Swap API — cURL example
# Docs: https://ai-engine.net/apis/face-swap

curl -X POST \
  'https://deepfake-face-swap-ai.p.rapidapi.com/swap-face' \
  -H 'x-rapidapi-host: deepfake-face-swap-ai.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'source_url=https://openmediadata.s3.eu-west-3.amazonaws.com/faceswap_api_demo_source.jpg&target_url=https://openmediadata.s3.eu-west-3.amazonaws.com/faceswap_api_demo_group.jpg'
