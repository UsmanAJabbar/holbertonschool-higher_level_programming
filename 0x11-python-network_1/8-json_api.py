#!/usr/bin/python3
"""A RANDOM COMMENT"""


if __name__ == "__main__":
    from sys import argv
    import requests

    # Setup variables/data
    try:
        url, char = 'http://0.0.0.0:5000/search_user', argv[1]
    except IndexError:
        url, char = 'http://0.0.0.0:5000/search_user', ""
    parameters = {'q': char}

    # Connection
    response = requests.post(url, data=parameters)

    # Analyze JSON
    try:
        out = response.json()
        if out == {} or None:
            print('No result')
        else:
            id = out['id']
            name = out['name']
            print('[{}] {}'.format(id, name))

    except Exception:
        print('Not a valid JSON')
