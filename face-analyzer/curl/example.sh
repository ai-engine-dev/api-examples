#!/bin/bash
# Face Analyzer API — cURL example
# Docs: https://ai-engine.net/apis/face-analyzer

curl -X POST \
  'https://faceanalyzer-ai.p.rapidapi.com/faceanalysis' \
  -H 'x-rapidapi-host: faceanalyzer-ai.p.rapidapi.com' \
  -H 'x-rapidapi-key: YOUR_API_KEY' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/face.jpg'
