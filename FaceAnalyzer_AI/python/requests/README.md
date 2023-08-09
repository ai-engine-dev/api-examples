# FaceAnalyzer AI samples

This directory contains a minimalistic samples that sends requests to the FaceAnalyzer AI API.
The samples is implemented in `python` using [requests](https://pypi.org/project/requests/) module.

## Overview

This API processes images and performs advanced facial analysis for face detection, age estimation, emotion analysis, celebrities identification, face comparison, and face re-identification.

## Getting started

Preinstall dependencies before use:

```bash
pip3 install -r requirements.txt
```

### Face analysis, detect and comparison:

Face Analysis

```bash
python3 face_analysis.py
```

Celebrities recognition

```bash
python3 celebrity_recognition.py
```

Compare Faces

```bash
python3 compare_faces.py
```

### Face Re-identification:


Create facial repository

```bash
python3 create_facial_repository.py
```

Delete facial repository

```bash
python3 delete_facial_repository.py
```

List facial repositories

```bash
python3 list_facial_repositories.py
```

List repository faces

```bash
python3 list_repository_faces.py
```

Save face in repository

```bash
python3 save_face_in_repository.py
```

Delete face from repository

```bash
python3 delete_facial_repository.py
```

Search face in repository

```bash
python3 search_face_in_repository.py
```


## API keys

Use [RapidAPI marketplace](https://rapidapi.com/ai-engine-ai-engine-default/api/faceanalyzer-ai/details) to get the API key. The marketplace offers both
free and paid subscriptions.

[Contact us](http://127.0.0.1:5173/contact) in case of any questions or to request a custom pricing plan
that better meets your business requirements.


