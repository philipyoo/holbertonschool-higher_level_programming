#!/usr/bin/python3
# Fetch from given URL using `urllib` package
import urllib.request

if __name__ == "__main__":
    print("Body response:")
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        content = res.read()
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        checker = res.headers.get_content_charset()
        if checker == "utf-8":
            print("\t- utf8 content: OK")
