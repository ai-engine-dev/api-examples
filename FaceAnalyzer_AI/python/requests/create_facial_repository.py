#!/usr/bin/env python3

"""Example of using AI-Engine FaceAnalyzer AI """

import os
import requests
import argparse

url = 'https://faceanalyzer-ai.p.rapidapi.com/create-facial-repository'
RAPIDAPI_KEY = 'YOUR_RAPIDAPI_KEY'
headers= {'X-RapidAPI-Key': RAPIDAPI_KEY}



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='invoke create-facial-repository endpoint')

    # Add arguments to the parser
    parser.add_argument('--repository_id', type=str, help='repository id', default='repository_id_example')
    args = parser.parse_args()
    
    data = {"repository_id": args.repository_id}
    response = requests.post(url, data=data, headers=headers)
    print(f'Raw response:\n{response.json()}\n')

    
