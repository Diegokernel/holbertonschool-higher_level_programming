#!/usr/bin/python3
"""takes your Github credentials (username and password) and uses the Github API to display your id"""
import requests
import sys

if __name__ == "__main__":
    page = "https://api.github.com/user"
    q = (sys.argv[1], sys.argv[2])
    req = requests.get(page, auth=q)
    print(req.json().get("id"))
