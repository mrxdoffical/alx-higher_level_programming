#!/usr/bin/python3
import urllib.request
import sys

"""fetching the x-request-id"""


def fetch_request_id(url):
    """
    Fetch the 'X-Request-Id' from the HTTP response headers of a given URL.

    Args:
        url (str): The URL from which to fetch the HTTP response.

    Returns:
        str: The value of the 'X-Request-Id' header, if present. None otherwise.
    """
    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get('X-Request-Id')
        return request_id

if __name__ == "__main__":
    url = sys.argv[1]
    request_id = fetch_request_id(url)
    print(request_id)
