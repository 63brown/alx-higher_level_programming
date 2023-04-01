#!/usr/bin/python3
"""A script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json_obj = response.json()
        id = json_obj.get('id')
        name = json_obj.get('name')
        if len(json_obj) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(json_obj.get('id'), json_obj.get('name')))
    except (Exception):
        print("Not a valid JSON")
