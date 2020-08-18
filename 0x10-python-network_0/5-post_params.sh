#!/bin/bash
# Send a POST request at that specific URL with email and parameters pre-defined
curl -s "$1" -X POST -F 'subject=I will always be here for PLD' -F 'email="hr@holbertonschool.com"'
