#!/usr/bin/python3
# Take in a URL, send request to URL and display value of `X-Request-Id`
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.info()['X-Request-Id'])
