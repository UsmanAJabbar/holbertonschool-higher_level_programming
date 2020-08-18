#!/bin/bash
# Send a request to a valid URL in $1 and extracts the content-length
curl -sI "$1" | grep Allow | awk '{ print $2 }'
