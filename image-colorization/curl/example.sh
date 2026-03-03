#!/bin/bash
# Image Colorization API — cURL example
# Docs: https://ai-engine.net/apis/image-colorization

curl -X POST \
  'https://photocolorizer-ai.p.rapidapi.com/colorize-photo' \
  -H 'x-rapidapi-host: photocolorizer-ai.p.rapidapi.com' \
  -H 'x-rapidapi-key: YOUR_API_KEY' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/bw-portrait.jpg'
