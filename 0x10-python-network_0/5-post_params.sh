#!/bin/bash
# Send a POST request at that specific URL with email and parameters pre-defined
curl -s "$1" -X POST -F 'email=hr@holbertonschool.com' -F 'subject=I will always be here for PLD'
