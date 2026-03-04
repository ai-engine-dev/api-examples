#!/bin/bash
# Face Analyzer API — cURL example
# Docs: https://ai-engine.net/apis/face-analyzer

curl -X POST \
  'https://faceanalyzer-ai.p.rapidapi.com/faceanalysis' \
  -H 'x-rapidapi-host: faceanalyzer-ai.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=https://openmediadata.s3.eu-west-3.amazonaws.com/face.jpg'
