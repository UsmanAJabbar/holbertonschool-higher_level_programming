#!/bin/bash
# Finds a pesky wabbit dug under the server with
curl -sL 0.0.0.0:5000/catch_me -X PUT -F 'user_id=98' -H 'Origin: HolbertonSchool'; echo ""
