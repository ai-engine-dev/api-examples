#!/usr/bin/env python3

"""Example of using AI-Engine FaceAnalyzer AI """

import requests
import argparse
from urllib.parse import urlparse

url = 'https://faceanalyzer-ai.p.rapidapi.com/list-repository-faces'
RAPIDAPI_KEY = 'YOUR_RAPIDAPI_KEY'
headers= {'X-RapidAPI-Key': RAPIDAPI_KEY}




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='invoke list-repository-faces endpoint')

    # Add arguments to the parser
    parser.add_argument('--repository_id', type=str, help='repository id where the face will be saved', default='repository_id_example')
    args = parser.parse_args()

    params = {"repository_id": args.repository_id}
    response = requests.get(url, params=params, headers=headers)
    
    print(f'Raw response:\n{response.json()}\n')




