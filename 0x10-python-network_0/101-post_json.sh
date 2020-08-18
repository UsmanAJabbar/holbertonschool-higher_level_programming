#!/bin/bash
# Sends a JSON file to an address that validates the code
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"
