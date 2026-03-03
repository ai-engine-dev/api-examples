# Face Analyzer

Detect faces and analyze age, gender, emotions, and facial features.

- **Endpoint**: `POST https://faceanalyzer-ai.p.rapidapi.com/faceanalysis`
- **Response**: JSON with `body.faces[]` containing `boundingBox`, `facialFeatures` (AgeRange, Gender, Smile, Emotions), and `landmarks`
- [RapidAPI Page](https://rapidapi.com/ai-engine-ai-engine-default/api/faceanalyzer-ai)
- [Full Documentation](https://ai-engine.net/apis/face-analyzer)

## Examples

| Language | File |
|----------|------|
| cURL | [curl/example.sh](curl/example.sh) |
| Python | [python/example.py](python/example.py) |
| JavaScript | [javascript/example.mjs](javascript/example.mjs) |

## Getting an API Key

1. Go to [Face Analyzer on RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/faceanalyzer-ai)
2. Click **Subscribe** (free tier available)
3. Copy your API key and replace `YOUR_API_KEY` in the examples
