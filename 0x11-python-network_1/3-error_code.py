#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body of the response"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as r:
            print(r.read().decode())
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
