#!/bin/bash
# Image Colorization API — cURL example
# Docs: https://ai-engine.net/apis/image-colorization

curl -X POST \
  'https://photocolorizer-ai.p.rapidapi.com/colorize-photo' \
  -H 'x-rapidapi-host: photocolorizer-ai.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=https://openmediadata.s3.eu-west-3.amazonaws.com/pexels-suzy-hazelwood-5292049.jpg'
