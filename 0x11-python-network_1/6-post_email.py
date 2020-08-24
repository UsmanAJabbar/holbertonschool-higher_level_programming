#!/usr/bin/python3
"""SOME DOCSTRING"""


if __name__ == "__main__":
    from sys import argv
    import requests

    # Generate Variables / Parameters
    url, email = argv[1], argv[2]
    parameters = {'email': email}

    # Process data
    response = requests.post('url', parameters)
    print(response.text)
