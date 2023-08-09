#!/usr/bin/env python3

"""Example of using AI-Engine FaceAnalyzer AI """

import requests
import argparse
from urllib.parse import urlparse

url = 'https://faceanalyzer-ai.p.rapidapi.com/delete-face-from-repository'
RAPIDAPI_KEY = 'YOUR_RAPIDAPI_KEY'
headers= {'X-RapidAPI-Key': RAPIDAPI_KEY}




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='invoke delete-face-from-repository endpoint')

    # Add arguments to the parser
    parser.add_argument('--repository_id', type=str, help='repository id where the face will be saved', default='repository_id_example')
    parser.add_argument('--face_ids',  nargs='+', help='repository id where the face will be saved', default=[])
    args = parser.parse_args()

    data = {"repository_id": args.repository_id,
            "face_ids": args.face_ids}
    response = requests.post(url, data=data, headers=headers)
    
    print(f'Raw response:\n{response.json()}\n')




