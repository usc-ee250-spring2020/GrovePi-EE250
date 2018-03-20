"""EE 250L Lab 08 Ultrasonic Ranger 1 Publisher

This file is used by the instructor to publish the distance readings from 
either ultrasonic ranger 1 or ultrasonic ranger 2. Please refer to the lab 
handout for an illustration to understand the position of each ultrasonic 
ranger.
"""

# set to 1 to run test mode (i.e. running without an raspberry pi)
TEST = 0

import paho.mqtt.client as mqtt
import argparse
import time

import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are able to successfully `import grovepi`
sys.path.append('../../Software/Python/')

if TEST:
    print("Test Mode")
else:
    import grovepi

# Determines which digital port the ultrasonic ranger is plugged into (e.g. a 
# value of 4 would mean port D4)
grovepi_digital_port = 4

mqtt_broker_hostname = "eclipse.usc.edu"
mqtt_broker_port = 11000

ultrasonic_ranger1_topic = "ultrasonic_ranger1"
ultrasonic_ranger2_topic = "ultrasonic_ranger2"

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("expected two arguments")
        print("Usage example: `python3 ultrasonic_ranger_publisher.py -u 2`")
        sys.exit()

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--ultrasonicranger",
        help = "Specify which ultrasonic ranger to subscribe to (1 or 2)",
                            default = 1) 
    args = parser.parse_args()

    distance = 0

    if args.ultrasonicranger == '1':
        topic = ultrasonic_ranger1_topic
    elif args.ultrasonicranger == '2':
        topic = ultrasonic_ranger2_topic

    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(mqtt_broker_hostname, mqtt_broker_port, keepalive=60)
    # have paho.mqtt spawn a background thread for us
    client.loop_start()

    while True:
        if TEST:
            distance = (distance + 1) % 10
            time.sleep(0.2)
        else:
            #ultrasonicRead() has a 60ms delay
            distance = grovepi.ultrasonicRead(grovepi_digital_port) 
            time.sleep(0.130)

        print("topic: " + topic + ", distance (cm): " + str(distance))
        client.publish(topic, distance)
