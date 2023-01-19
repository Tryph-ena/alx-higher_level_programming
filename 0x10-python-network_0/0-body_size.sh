#!/bin/bash
# A script that takes in a URL and displays size in bytes
curl -s "$1" | wc -c
