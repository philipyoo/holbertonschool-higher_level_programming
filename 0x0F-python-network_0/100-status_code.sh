#!/bin/bash
# Send a request to a URL and display only status code of response with restrictions
curl -s -o /dev/null -w "%{http_code}" "$1"
