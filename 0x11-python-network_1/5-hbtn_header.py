#!/usr/bin/python3
"""Script that sends a request to the URL & displays the value of a variable"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    n = requests.get(url)
    print(n.headers.get("X-Request-Id"))
