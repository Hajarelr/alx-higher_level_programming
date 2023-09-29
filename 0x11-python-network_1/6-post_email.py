#!/usr/bin/python3
"""Script that sends a POST request to the URL & displays the response"""
import sys
import requests


if __name__ == "__main__":
    m = sys.argv[1]
    o = {"email": sys.argv[2]}

    n = requests.post(m, data=o)
    print(n.text)
