#!/usr/bin/env python3

"""Example of using AI-Engine FaceAnalyzer AI """

import os
import requests
import argparse

url = 'https://faceanalyzer-ai.p.rapidapi.com/list-facial-repositories'
RAPIDAPI_KEY = 'YOUR_RAPIDAPI_KEY'
headers= {'X-RapidAPI-Key': RAPIDAPI_KEY}



if __name__ == '__main__':

    response = requests.get(url, headers=headers)
    print(f'Raw response:\n{response.json()}\n')

    
