#!/usr/bin/python3
"""A script that takes 2 arguments.
The first argument will be the repository name.
The second argument will be the owner name in order.
You must use the packages requests and sys """
import requests
from sys import argv


if __name__ == '__main__':
    url = requests.get('https://api.github.com/repos/{}/{}/commits/'
                       .format(argv[2], argv[1]))
    response = requests.get(url)
    json_obj = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                json_obj[i].get("sha"),
                json_obj[i].get("commit").get("author").get("name")))
    except (Exception):
        pass
