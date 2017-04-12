#!/usr/bin/python3
"""
Use requests package to make a get request to the github api.
First argument is username, second argument is password.
"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2])).json()
    try:
        print(r['id'])
    except:
        print("None")
