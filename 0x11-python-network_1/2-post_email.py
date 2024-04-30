#!/usr/bin/python3
import sys
from urllib import request, parse

def send_post_request(url, email):
    # Data to be sent in the POST request
    data = parse.urlencode({'email': email}).encode()

    # Create a request object
    req = request.Request(url, data=data)  # 'data' automatically makes it a POST request

    # Send the request and read the response
    with request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print("Your email is: ", response_body)

if __name__ == "__main__":
    # Command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Call the function with the URL and email
    send_post_request(url, email)