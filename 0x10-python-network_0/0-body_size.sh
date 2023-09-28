#!/bin/bash
# Script that tales in a url sends a request to that url & displays the size
curl -s "$1" | wc -c
