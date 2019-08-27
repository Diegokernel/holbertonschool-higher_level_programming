#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body of the response."""
import requests
import sys

if __name__ == "__main__":
    r = requests.get('{}'.format(sys.argv[1]))
    if r.status_code is 200:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
