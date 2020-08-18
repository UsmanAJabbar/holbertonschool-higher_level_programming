#!/bin/bash
# Send a request to a valid URL in $1 and extracts the content-length
curl -s -o /dev/null -w "%{http_code}" "$1"
