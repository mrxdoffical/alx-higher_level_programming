#!/usr/bin/python3
import sys
import urllib.request


def fetch_request_id(url):
    """
    Sends a request to the given URL and retrieves the 'X-Request-Id' header 
    from the response.

    Parameters:
    url (str): The URL to which the request will be sent.

    Returns:
    str: The value of the 'X-Request-Id' header.
    """
    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get('X-Request-Id')
        return request_id


if __name__ == "__main__":
    # Assume the URL is passed as the first command line argument
    url = sys.argv[1]
    request_id = fetch_request_id(url)
    print(request_id)