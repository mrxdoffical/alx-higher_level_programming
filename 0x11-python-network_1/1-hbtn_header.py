#!/usr/bin/python3
import urllib.request
import sys

"""
This module is designed to fetch and print the 'X-Request-Id' header from a given URL.
It assumes the URL is provided as a command-line argument.
"""

def fetch_request_id(url):
    """Fetch the 'X-Request-Id' header from the specified URL."""
    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get('X-Request-Id')
        return request_id

if __name__ == "__main__":
    url = sys.argv[1]
    request_id = fetch_request_id(url)
    print(request_id)
