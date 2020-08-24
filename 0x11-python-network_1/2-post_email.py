#!/usr/bin/python3
"""SOME DOCSTRING"""


if __name__ == "__main__":
    from sys import argv
    import urllib.request
    import urllib.parse

    url, email = argv[1], argv[2]

    parameters = {'email': email}
    data = urllib.parse.urlencode(parameters)
    data = data.encode('ascii')
#    req = request.Request(url, data=data)

    with urllib.request.urlopen(url, data) as response:
        out = response.read()
        print(out.decode('utf-8'))
