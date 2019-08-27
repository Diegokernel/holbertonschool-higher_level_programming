#!/usr/bin/python3
"""  fetches https://intranet.hbtn.io/status  """
import requests
import sys

if __name__ == "__main__":
    html = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=html)
    print(r.text)
