import requests
import json
from datetime import datetime
import time

if __name__ == '__main__':

    # This header sets the HTTP request's mimetype to `application/json`. This
    # means the payload of the http packet will be formatted as a json ojbect
    hdr = {
        'Content-Type': 'application/json',
        'Authorization': None #not using HTTP secure
    }

    # The payload of our packet starts as a simple dictionary. Before sending
    # the HTTP packet, we will format this into a json object
    payload = {
        'time': str(datetime.now()),
        'event': "WALKING RIGHT"
    }

    while True:
        # Send the packet together and block until a response is given.
        response = requests.post("http://0.0.0.0:5000/post-event", headers = hdr,
                                 data = json.dumps(payload))

        # Print the json object from the HTTP response
        print(response.json())

        time.sleep(2)

