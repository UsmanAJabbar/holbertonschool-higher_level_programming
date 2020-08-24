#!/usr/bin/python3
"""MY GITHUB, VERY KEWL!!!"""


if __name__ == "__main__":
    from sys import argv
    import requests

    url, user, token = 'https://api.github.com/user', argv[1], argv[2]
    out = requests.get(url, auth=(user, token))

    try:
        id = (out.json()['id'])
        print(id)
    except KeyError:
        print('None')
