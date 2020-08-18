#!/bin/bash
# Sends a request to the URL with GET and a specific header
curl -s "$1" -H "X-HolbertonSchool-User-Id:98"
