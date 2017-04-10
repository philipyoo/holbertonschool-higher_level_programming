#!/bin/bash
# Takes in URL, sends GET request setting a header variable, display body
curl -sX "GET" -H "X-HolbertonSchool-User-Id: 98" "$1"
