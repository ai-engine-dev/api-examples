<p align="center">
  <img src="assets/logo.png" alt="AI Engine" width="80" />
</p>

<h1 align="center">AI Engine — API Examples</h1>

<p align="center">
  Code examples for <a href="https://ai-engine.net">AI Engine</a> APIs — computer vision, OCR, and image processing.<br/>
  All APIs are available on <a href="https://rapidapi.com/organization/ai-engine">RapidAPI</a> with a free tier.
</p>

---

## APIs

| API | Description | RapidAPI |
|-----|-------------|----------|
| [Background Removal](background-removal/) | Remove backgrounds from images and get a clean transparent PNG. | [Subscribe](https://rapidapi.com/ai-engine-ai-engine-default/api/background-removal-ai) |
| [Emotion & Personality Analysis](emotion-analysis/) | Detect emotions and personality traits from text. | [Subscribe](https://rapidapi.com/ai-engine-ai-engine-default/api/emotion-sentiment-personality-analysis) |
| [Face Analyzer](face-analyzer/) | Detect faces and analyze age, gender, emotions, and facial features. | [Subscribe](https://rapidapi.com/ai-engine-ai-engine-default/api/faceanalyzer-ai) |
| [Face Restoration](face-restoration/) | Restore and enhance old, blurry, or low-quality face photos. | [Subscribe](https://rapidapi.com/ai-engine-ai-engine-default/api/face-restoration) |
| [Face Swap](face-swap/) | Swap faces between two images using AI. | [Subscribe](https://rapidapi.com/ai-engine-ai-engine-default/api/deepfake-face-swap-ai) |
| [Image Colorization](image-colorization/) | Colorize black-and-white photos with AI. | [Subscribe](https://rapidapi.com/ai-engine-ai-engine-default/api/photocolorizer-ai) |
| [Image Generation](image-generation/) | Generate images from text prompts using AI. | [Subscribe](https://rapidapi.com/ai-engine-ai-engine-default/api/imagegenius-ai) |
| [Label Image](label-image/) | Auto-tag images with descriptive labels and confidence scores. | [Subscribe](https://rapidapi.com/ai-engine-ai-engine-default/api/label-image) |
| [Landmark Detection](landmark-detection/) | Identify famous landmarks in photos with GPS coordinates. | [Subscribe](https://rapidapi.com/ai-engine-ai-engine-default/api/landmarks-detection) |
| [Logo Detection](logo-detection/) | Detect brand logos in images. | [Subscribe](https://rapidapi.com/ai-engine-ai-engine-default/api/logos-detection) |
| [Mask Detection](mask-detection/) | Detect whether people are wearing face masks. | [Subscribe](https://rapidapi.com/ai-engine-ai-engine-default/api/mask-detection2) |
| [NSFW Detect](nsfw-detect/) | Detect NSFW/inappropriate content in images for content moderation. | [Subscribe](https://rapidapi.com/ai-engine-ai-engine-default/api/nsfw-detect3) |
| [Object Detection](object-detection/) | Detect and locate objects in images with bounding boxes. | [Subscribe](https://rapidapi.com/ai-engine-ai-engine-default/api/objects-detection) |
| [OCR Wizard](ocr-wizard/) | Extract text from images with support for 200+ languages and handwriting. | [Subscribe](https://rapidapi.com/ai-engine-ai-engine-default/api/ocr-wizard) |
| [Photo to Anime](photo-to-anime/) | Transform photos into anime, cartoon, or sketch styles. | [Subscribe](https://rapidapi.com/ai-engine-ai-engine-default/api/phototoanime1) |
| [PPE Detection](ppe-detection/) | Detect personal protective equipment (helmets, masks, gloves) on people. | [Subscribe](https://rapidapi.com/ai-engine-ai-engine-default/api/ppe-detection1) |

## Getting Started

1. Create a free account on [RapidAPI](https://rapidapi.com/)
2. Subscribe to any [AI Engine API](https://rapidapi.com/organization/ai-engine) (free tier available)
3. Copy your API key from the RapidAPI dashboard
4. Set your API key as an environment variable:

```bash
export RAPIDAPI_KEY="your_api_key_here"
```

5. Run any example:

```bash
# cURL
bash background-removal/curl/example.sh

# Python
python3 background-removal/python/example.py

# JavaScript (Node.js 18+)
node background-removal/javascript/example.mjs
```

All examples read the `RAPIDAPI_KEY` environment variable automatically. You can also replace `YOUR_API_KEY` directly in the code if you prefer.

## Structure

Each API folder contains working examples in three languages:

```
api-name/
├── README.md              # API description and response format
├── curl/example.sh        # cURL
├── python/example.py      # Python (requests)
└── javascript/example.mjs # Node.js (fetch)
```

## Requirements

- **cURL**: any modern version
- **Python**: 3.7+ with `requests` (`pip install requests`)
- **Node.js**: 18+ (uses native `fetch`)

## Links

- [AI Engine Website](https://ai-engine.net)
- [Blog & Tutorials](https://ai-engine.net/blog)
- [All APIs on RapidAPI](https://rapidapi.com/organization/ai-engine)
- [Contact](mailto:contact@ai-engine.net)

## License

MIT
