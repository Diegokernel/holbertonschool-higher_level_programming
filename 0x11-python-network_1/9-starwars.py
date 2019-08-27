#!/usr/bin/python3
"""takes in a string and sends a search request to the Star Wars API"""
import requests
import sys

if __name__ == "__main__":
    page = "https://swapi.co/api/people/"
    q = {'search': sys.argv[1]}
    r = requests.get(page, params=q)
    counting = r.json().get('count')
    print("Number of results: {}".format(counting))
    result = r.json().get("results")

    for response in range(len(result)):
        print(result[response].get("name"))
