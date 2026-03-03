#!/bin/bash
# OCR Wizard API — cURL example
# Docs: https://ai-engine.net/apis/ocr-wizard

curl -X POST \
  'https://ocr-wizard.p.rapidapi.com/ocr' \
  -H 'x-rapidapi-host: ocr-wizard.p.rapidapi.com' \
  -H 'x-rapidapi-key: YOUR_API_KEY' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'url=https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/text.jpg'
