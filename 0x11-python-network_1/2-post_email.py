#!/usr/bin/python3


if __name__ == "__main__":
    from sys import argv
    from urllib import request, parse

    url, email = argv[1], argv[2]

    parameters = {'email': email}
    data = parse.urlencode(parameters)
    data = data.encode('ascii')
#    req = request.Request(url, data=data)

    with request.urlopen(url, data) as response:
        out = response.read()
        print(out.decode('utf-8'))
