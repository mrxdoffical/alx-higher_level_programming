#!/usr/bin/python3
import urllib.request

# URL to fetch
url = "https://alx-intranet.hbtn.io/status"

# Use urllib to open the URL
with urllib.request.urlopen(url) as response:
    # Read the response body as bytes
    body = response.read()

    # Print the formatted output with `$` at the end of each line
    # print("Body response:$")
    print((type(body)))
    print((body))
    print((body.decode('utf-8')))