#!/usr/bin/python3
"""takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        q = ""
    else:
        q = "{}".format(sys.argv[1])
        r = requests.post(url, data={"q": q})
        try:
            des = r.json()
            if len(des) == 0:
                print("No result")
            else:
                print("[{}] {}".format(des.get("id"), des.get("name")))
        except ValueError:
            print("Not a valid JSON")
