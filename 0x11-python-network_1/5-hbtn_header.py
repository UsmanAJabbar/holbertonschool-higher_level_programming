#!/usr/bin/python3
"""ANOTHER COMMENT"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    response = requests.get(url)
    value = response.headers.get('X-Request-Id')
    print(value)
