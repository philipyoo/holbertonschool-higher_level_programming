#!/bin/bash
# Take in URL, send POST request setting some params, display body
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be there for PLD" "$1"
