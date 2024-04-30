#!/usr/bin/python3
import urllib.request
import sys

"""
This module is designed to fetch and print the 'X-Request-Id' header from a given URL.
It is intended to be used as a command-line tool where the URL is provided as an argument.

Dependencies:
- urllib.request for handling the HTTP requests.
- sys for accessing command-line arguments.

Usage:
    python fetch_request_id.py [URL]
    Example: python fetch_request_id.py http://example.com
"""

def fetch_request_id(url):
    """
    Fetch the 'X-Request-Id' header from the specified URL.

    Parameters:
    - url (str): The URL from which to fetch the 'X-Request-Id' header.

    Returns:
    - str: The value of the 'X-Request-Id' header, or None if the header is not found.

    Raises:
    - urllib.error.URLError: An error from urllib.request.urlopen if the URL is incorrect or unreachable.
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