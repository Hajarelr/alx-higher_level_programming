#!/usr/bin/python3
"""Script that takes 2 arguments to solve the challenge of HS"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for n in range(10):
            print("{}: {}".format(
                commits[n].get("sha"),
                commits[n].get("commit").get("author").get("name")))
    except IndexError:
        pass
