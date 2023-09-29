#!/usr/bin/python3
""" Script that takes in a URL and sends a request to the URL"""


import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
    except:
        pass
