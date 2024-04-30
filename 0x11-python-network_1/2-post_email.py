import sys
from urllib import request, parse

def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the given email.

    Parameters:
        url (str): The URL to which the POST request is sent.
        email (str): The email address to be sent as a part of the POST request.

    Prints:
        The body of the response, decoded in utf-8.
    """
    # Data to be sent in the POST request
    data = parse.urlencode({'email': email}).encode()

    # Create a request object
    req = request.Request(url, data=data)  # 'data' automatically makes it a POST request

    # Send the request and read the response
    with request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)

if __name__ == "__main__":
    """
    Main execution point of the script. Takes a URL and an email from the command line,
    sends a POST request to the URL with the email as a parameter, and prints the response.
    """
    # Command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Call the function with the URL and email
    send_post_request(url, email)