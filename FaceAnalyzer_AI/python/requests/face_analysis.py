#!/usr/bin/env python3

"""Example of using AI-Engine FaceAnalyzer AI """

import requests
import argparse
from urllib.parse import urlparse

url = 'https://faceanalyzer-ai.p.rapidapi.com/faceanalysis'
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
    image_bytes = None
    with open(image_path, 'rb') as file:
        image_bytes = file.read()
    return image_bytes




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='invoke faceanalysis endpoint')

    # Add arguments to the parser
    parser.add_argument('--image', type=str, help='could be the local path of the image or an image url', default='https://openmediadata.s3.eu-west-3.amazonaws.com/face_open_data.jpg')
    args = parser.parse_args()
    
    if(not is_url(args.image)):
        image_bytes = load_image_bytes(args.image)
        files = {"image": image_bytes}
        response = requests.post(url, files=files, headers=headers)
        print(f'Raw response:\n{response.json()}\n')
    else:
        data = {"url": args.image}
        response = requests.post(url, data=data, headers=headers)
        print(f'Raw response:\n{response.json()}\n')




