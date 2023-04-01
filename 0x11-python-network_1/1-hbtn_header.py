#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response"""
import urllib.request as request
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        info = response.info()
        print(info.get("X-Request-Id"))
