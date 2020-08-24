#!/usr/bin/python3
"""A DOCSTRING"""

if __name__ == "__main__":
    from sys import argv
    from urllib.error import HTTPError
    from urllib.request import urlopen

    try:
        url = argv[1]
        with urlopen(url) as response:
            out = response.read()
            content = out.decode('utf-8')
            print(content)

    except HTTPError as error:
        status_code = str(error).split(' ')[2].replace(':', '')
        print('Error code: ' + status_code)
