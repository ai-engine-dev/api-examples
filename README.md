<p align="center">
  <img src="assets/logo.png" alt="AI Engine" width="80" />
</p>

<h1 align="center">AI Engine API Examples</h1>

<p align="center">
  Ready-to-run cURL, Python and Node.js examples for the <a href="https://ai-engine.net?utm_source=github&utm_medium=referral&utm_campaign=api-examples">AI Engine</a> image and text APIs.
</p>

## Quick start

```bash
git clone https://github.com/ai-engine-dev/api-examples.git
cd api-examples
export RAPIDAPI_KEY="your_api_key"
python3 background-removal/python/example.py
```

Get a key by subscribing to any API below on RapidAPI (every API has a free plan). The examples read `RAPIDAPI_KEY` from your environment, so your key never ends up in the code.

## APIs


### Faces and identity

| API | What it does | Docs | Key |
|-----|--------------|------|-----|
| [Face Analyzer](face-analyzer/) | Detect faces, estimate age, gender and emotion, compare and search faces | [ai-engine.net](https://ai-engine.net/apis/face-analyzer?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/faceanalyzer-ai) |
| [Face Swap](face-swap/) | Swap a face into a photo | [ai-engine.net](https://ai-engine.net/apis/face-swap?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/deepfake-face-swap-ai) |
| [Face Restoration](face-restoration/) | Restore blurry or old face photos | [ai-engine.net](https://ai-engine.net/apis/face-restoration?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/face-restoration) |

### Image editing

| API | What it does | Docs | Key |
|-----|--------------|------|-----|
| [Background Removal](background-removal/) | Remove the background, or replace it with a color, blur, gradient or image | [ai-engine.net](https://ai-engine.net/apis/background-removal?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/background-removal-ai) |
| [Image Colorization](image-colorization/) | Colorize black and white photos | [ai-engine.net](https://ai-engine.net/apis/image-colorization?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/photocolorizer-ai) |
| [Photo to Anime](photo-to-anime/) | Turn photos into anime or cartoon style | [ai-engine.net](https://ai-engine.net/apis/photo-to-anime?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/phototoanime1) |
| [Photo to Portrait](photo-to-portrait/) | Turn photos into pencil sketch portraits | [ai-engine.net](https://ai-engine.net/apis/photo-to-portrait?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/phototoportrait) |
| [Image Generation](image-generation/) | Generate images from text prompts | [ai-engine.net](https://ai-engine.net/apis/image-generation?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/imagegenius-ai) |

### Moderation and safety

| API | What it does | Docs | Key |
|-----|--------------|------|-----|
| [NSFW Detect](nsfw-detect/) | Flag nudity, violence and other unsafe content | [ai-engine.net](https://ai-engine.net/apis/nsfw-detect?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/nsfw-detect3) |
| [Mask Detection](mask-detection/) | Check who is wearing a face mask | [ai-engine.net](https://ai-engine.net/apis/mask-detection?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/mask-detection2) |
| [PPE Detection](ppe-detection/) | Check head, face and hand protection on workers | [ai-engine.net](https://ai-engine.net/apis/ppe-detection?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/ppe-detection1) |

### Detection and text

| API | What it does | Docs | Key |
|-----|--------------|------|-----|
| [OCR Wizard](ocr-wizard/) | Extract text from images, with handwriting support | [ai-engine.net](https://ai-engine.net/apis/ocr-wizard?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/ocr-wizard) |
| [Object Detection](object-detection/) | Detect and locate objects with bounding boxes | [ai-engine.net](https://ai-engine.net/apis/object-detection?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/objects-detection) |
| [Label Image](label-image/) | Tag images with labels and confidence scores | [ai-engine.net](https://ai-engine.net/apis/label-image?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/label-image) |
| [Logo Detection](logo-detection/) | Detect brand logos | [ai-engine.net](https://ai-engine.net/apis/logo-detection?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/logos-detection) |
| [Landmark Detection](landmark-detection/) | Recognize landmarks with GPS coordinates | [ai-engine.net](https://ai-engine.net/apis/landmark-detection?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/landmarks-detection) |
| [Emotion Analysis](emotion-analysis/) | Emotion, sentiment and personality from text | [ai-engine.net](https://ai-engine.net/apis/emotion-analysis?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/emotion-sentiment-personality-analysis) |

### One key for everything

[AI All-in-One](all-in-one/) gives you 36+ endpoints (OCR, faces, backgrounds, restoration, moderation, text analysis) with a single subscription. [Docs](https://ai-engine.net/apis/all-in-one?utm_source=github&utm_medium=referral&utm_campaign=api-examples) | [RapidAPI](https://rapidapi.com/ai-engine-ai-engine-default/api/ai-all-in-one)

## Run an example

```bash
# cURL
bash ocr-wizard/curl/example.sh

# Python 3.7+ (pip install requests)
python3 ocr-wizard/python/example.py

# Node.js 18+
node ocr-wizard/javascript/example.mjs
```

Each folder has the same layout:

```
api-name/
├── README.md               endpoint and response format
├── curl/example.sh
├── python/example.py
└── javascript/example.mjs
```

## Tutorials

- [Best background removal APIs compared](https://ai-engine.net/blog/best-background-removal-apis?utm_source=github&utm_medium=referral&utm_campaign=api-examples)
- [Background removal for product catalogs at scale](https://ai-engine.net/blog/background-removal-at-scale-ecommerce?utm_source=github&utm_medium=referral&utm_campaign=api-examples)
- [Face swap API guide](https://ai-engine.net/blog/face-swap-api-guide?utm_source=github&utm_medium=referral&utm_campaign=api-examples)
- [KYC selfie verification with a face API](https://ai-engine.net/blog/identity-verification-face-api?utm_source=github&utm_medium=referral&utm_campaign=api-examples)
- [Best NSFW detection APIs compared](https://ai-engine.net/blog/best-nsfw-detection-apis-compared?utm_source=github&utm_medium=referral&utm_campaign=api-examples)
- [OCR a PDF in 5 lines of Python](https://ai-engine.net/blog/pdf-ocr-python-5-lines?utm_source=github&utm_medium=referral&utm_campaign=api-examples)
- [More on the blog](https://ai-engine.net/blog?utm_source=github&utm_medium=referral&utm_campaign=api-examples)

## Links

- [All APIs](https://ai-engine.net/apis?utm_source=github&utm_medium=referral&utm_campaign=api-examples)
- [Contact](mailto:contact@ai-engine.net)

## License

MIT
