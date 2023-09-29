#!/usr/bin/python3
"""Scrit that sends a POST request to http://0.0.0.0:5000/search_user"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    payload = {'q': letter}

    request = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        response = request.json()
        if response == {}:
            print('No result')
        else:
            print('[{}] {}'.format(response.get('id'), response.get('name')))
    except ValueError:
        print('Not a valid JSON')