#!/bin/bash
# Script to take a URL, send request to URL, and display size of body response
curl -sI "$1" | grep Content-Length | cut -d " " -f2
