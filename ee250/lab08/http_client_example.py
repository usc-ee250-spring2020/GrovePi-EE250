import requests
import json
from datetime import datetime
import time

"""This file illustrates the typical calls you need from an http client. 
More specifically, in your signal_processing.py code, you should have a
request.post() call everytime a movement is classified by your algorithm."""

if __name__ == '__main__':

    # This header sets the HTTP request's mimetype to `application/json`. This
    # means the payload of the HTTP message will be formatted as a json ojbect
    hdr = {
        'Content-Type': 'application/json',
        'Authorization': None #not using HTTP secure
    }

    # The payload of our message starts as a simple dictionary. Before sending
    # the HTTP message, we will format this into a json object
    payload = {
        'time': str(datetime.now()),
        'event': "Moving Right"
    }

    while True:
        # Send an HTTP POST message and block until a response is given.
        # Note: requests() is NOT the same thing as request() under the flask 
        # library.
        response = requests.post("http://0.0.0.0:5000/post-event", headers = hdr,
                                 data = json.dumps(payload))

        # Print the json object from the HTTP response
        print(response.json())

        time.sleep(2)

