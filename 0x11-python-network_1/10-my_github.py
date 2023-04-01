#!/usr/bin/python3
"""A script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get('https://api.github.com/user',
                            auth=HTTPBasicAuth(username, password))
    print(response.json().get("id"))
