#!/bin/bash
# NSFW Detect API — cURL example
# Docs: https://ai-engine.net/apis/nsfw-detect

curl -X POST \
  'https://nsfw-detect3.p.rapidapi.com/nsfw-detect' \
  -H 'x-rapidapi-host: nsfw-detect3.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=https://raw.githubusercontent.com/ai-engine-dev/api-examples/master/assets/samples/street.jpg'
