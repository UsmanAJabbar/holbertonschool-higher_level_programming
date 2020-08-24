#!/usr/bin/python3
"""A WILD COMMENT APPEARS"""


if __name__ == "__main__":
    from sys import argv
    import requests

    url, owner, repo = "https://api.github.com/repos/", argv[1], argv[2]

    response1 = requests.get(url + owner + '/' + repo + '/commits')
    dictionary = response1.json()

    count = 0
    for elements in dictionary:
        print(elements['sha'], elements['commit']['author']['name'])
        count += 1
        if count == 10:
            break
