#!/usr/bin/python3
"""ANOTHER COMMENT"""


if __name__ == "__main__":
    from urllib import request
    from sys import argv

    with request.urlopen(argv[1]) as response:
        value = response.getheader('X-Request-Id')
        print(value)
