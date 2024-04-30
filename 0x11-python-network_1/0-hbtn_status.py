import urllib.request

# URL to fetch
url = "https://alx-intranet.hbtn.io/status"

# Use urllib to open the URL
with urllib.request.urlopen(url) as response:
    # Read the response body as bytes
    body = response.read()

    # Print the formatted output
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))