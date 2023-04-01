#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)"""
import urllib.request as request
import urllib.error as error
from sys import argv


if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            print(str(response.read(), 'utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.getcode()))
