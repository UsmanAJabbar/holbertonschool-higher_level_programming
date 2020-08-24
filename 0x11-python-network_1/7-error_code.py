#!/usr/bin/python3
"""A DOCSTRING"""


if __name__ == "__main__":
    from sys import argv
    import requests

    url = argv[1]
    out = requests.get(url)
    status_code = out.status_code
    content = out.text

    if status_code >= 400:
        print('Error code: ' + str(status_code))
    else:
        print(content)
