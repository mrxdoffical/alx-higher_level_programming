#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]
then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Use curl to fetch the HTTP status code
status_code=$(curl -o /dev/null -s -w "%{http_code}" "$1")

# Display the status code
echo $status_code