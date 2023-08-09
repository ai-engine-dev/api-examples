#!/usr/bin/env python3

"""Example of using AI-Engine FaceAnalyzer AI """

import os
import requests
import argparse
from urllib.parse import urlparse

url = 'https://faceanalyzer-ai.p.rapidapi.com/compare-faces'
RAPIDAPI_KEY = 'YOUR_RAPIDAPI_KEY'
headers= {'X-RapidAPI-Key': RAPIDAPI_KEY}

def is_url(string):
    # Parse the URL
    parsed_url = urlparse(string)

    # Check if the scheme and netloc are not empty
    if parsed_url.scheme and parsed_url.netloc:
        return True
    else:
        return False

def load_image_bytes(image_path):
    if(not os.path.exists(image_path)):
        print(f"{image_path} not found")
        exit(1)
    image_bytes = None
    with open(image_path, 'rb') as file:
        image_bytes = file.read()
    return image_bytes




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='invoke compare-faces endpoint')

    # Add arguments to the parser
    parser.add_argument('--source_image', type=str, help='could be the local path of the image or an image url', default='https://openmediadata.s3.eu-west-3.amazonaws.com/face_open_data.jpg')
    parser.add_argument('--target_image', type=str, help='could be the local path of the image or an image url', default='https://openmediadata.s3.eu-west-3.amazonaws.com/face_open_data.jpg')
    args = parser.parse_args()
    
    files = {}
    data = {}
    if(not is_url(args.source_image)):
        image_bytes = load_image_bytes(args.source_image)
        files = {"source_image": image_bytes}
    else:
        data = {"source_image_url": args.source_image}

    if(not is_url(args.target_image)):
        image_bytes = load_image_bytes(args.target_image)
        files = {**files, **{"target_image": image_bytes}}
    else:
        data = {**data, **{"target_image_url": args.target_image}}
    
    response = requests.post(url, files=files, data=data, headers=headers)
    print(f'Raw response:\n{response.json()}\n')

    
