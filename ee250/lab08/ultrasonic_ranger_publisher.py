"""EE 250L Lab 08 Ultrasonic Ranger 1 Publisher

This file is used by the instructor to publish the distance readings from 
either ultrasonic ranger 0 or ultrasonic ranger 1. Please refer to the lab 
handout for an illustration to understand the position of each ultrasonic 
ranger.
"""

import paho.mqtt.client as mqtt
import argparse

import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are able to successfully `import grovepi`
sys.path.append('../../Software/Python/')

import grovepi

# Determines which port the ultrasonic ranger is plugged into (e.g. a value of
# 4 would mean port D4)
grove_digital_port = 4

mqtt_broker_hostname = "eclipse.usc.edu"
mqtt_broker_port = 11000

U0_topic = "ultrasonic-ranger0"
U1_topic = "ultrasonic-ranger1"

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--ultrasonicranger",
        help = "Specify 0 for ultrasonic ranger 0 and 1 for ultrasonic ranger 1",
                            default = 0) 

    args = parser.parse_args()

    if args.ultrasonicranger == '0':
        topic = U0_topic
    elif args.ultrasonicranger == '1':
        topic = U1_topic

    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(mqtt_broker_hostname, mqtt_broker_port, keepalive=60)
    # have paho.mqtt spawn a background thread for us
    client.loop_start()

    while True:
        distance = grovepi.ultrasonicRead(grove_digital_port) 
        print("distance (cm): " + str(distance))
        client.publish(topic, distance)


