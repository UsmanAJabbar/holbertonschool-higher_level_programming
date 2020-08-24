#!/usr/bin/python3
"""A DUMB COMMENT"""


if __name__ == "__main__":
    import requests

    response = requests.get('https://intranet.hbtn.io/status')
    page = response.text
    print('Body response:')
    print("\t- type: {}".format(type(page)))
    print("\t- content: {}".format(page))
