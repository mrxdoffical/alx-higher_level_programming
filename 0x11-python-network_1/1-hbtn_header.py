#!/usr/bin/python3
import urllib
import sys
import urllib.request

"""fetching the requested url"""

def fetch_request_id(url):

    """fetching the requested url"""

    with urllib.request.urlopen(url) as response:
        # Retrieve the X-Request-Id header value
        request_id = response.headers.get('X-Request-Id')
        return request_id

if __name__ == "__main__":
    # Assume the URL is passed as the first command line argument
    url = sys.argv[1]
    request_id = fetch_request_id(url)
    print(request_id)
