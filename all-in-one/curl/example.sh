#!/bin/bash
# AI All-in-One API: cURL example
# Docs: https://ai-engine.net/apis/all-in-one

# Extract text from an image
curl -X POST \
  'https://ai-all-in-one.p.rapidapi.com/v1/ocr' \
  -H 'x-rapidapi-host: ai-all-in-one.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=https://openmediadata.s3.eu-west-3.amazonaws.com/pexels-monstera-5709059.jpg'

# Same key, another endpoint: sentiment of a review
curl -X POST \
  'https://ai-all-in-one.p.rapidapi.com/v1/sentiment' \
  -H 'x-rapidapi-host: ai-all-in-one.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'text=I love this product, it works great'
