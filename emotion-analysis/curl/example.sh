#!/bin/bash
# Emotion & Personality Analysis API — cURL example
# Docs: https://ai-engine.net/apis/emotion-analysis

curl -X POST \
  'https://emotion-sentiment-personality-analysis.p.rapidapi.com/emotions' \
  -H 'x-rapidapi-host: emotion-sentiment-personality-analysis.p.rapidapi.com' \
  -H "x-rapidapi-key: ${RAPIDAPI_KEY:-YOUR_API_KEY}" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'text=I am so happy today! The weather is beautiful and I feel great.'
