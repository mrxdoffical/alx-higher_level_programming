#!/usr/bin/python3
import urllib.request
import sys

"""
This module is designed to fetch and print the
"""

def fetch_request_id(url):
    """
    Fetch the 'X-Request-Id' header from the specified URL.

    """
    with urllib.request.urlopen(url) as response:
        # Extract the 'X-Request-Id' header from the response
        request_id = response.headers.get('X-Request-Id')
        return request_id

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_request_id.py [URL]")
        sys.exit(1)
    url = sys.argv[1]
    try:
        request_id = fetch_request_id(url)
        print(request_id)
    except Exception as e:
        print(f"Error fetching the 'X-Request-Id' header: {e}")