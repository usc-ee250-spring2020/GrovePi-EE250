"""EE 250L Lab 10 Ultrasonic Ranger 1 Publisher

This file is used by the instructor to publish the distance readings from 
either ultrasonic ranger 1 or ultrasonic ranger 2. Please refer to the lab 
handout for an illustration to understand the position of each ultrasonic 
ranger.
"""

# set to 1 to run test mode (i.e. running without an raspberry pi)
TEST = 1 

import paho.mqtt.client as mqtt
import argparse
import time
# Import SPI library (for hardware SPI) and MCP3008 library.
import random
import sys

if TEST:
    print("Test Mode")
    ultrasonic_ranger1_topic = "ultrasonic_ranger1/fake_data"
    ultrasonic_ranger2_topic = "ultrasonic_ranger2/fake_data"
else:
    import Adafruit_GPIO.SPI as SPI
    import Adafruit_MCP3008
    #Hardware SPI configuration:
    SPI_PORT   = 0
    SPI_DEVICE = 0
    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
    ultrasonic_ranger1_topic = "ultrasonic_ranger1/real_data"
    ultrasonic_ranger2_topic = "ultrasonic_ranger2/real_data"


mqtt_broker_hostname = "eclipse.usc.edu"
mqtt_broker_port = 11000


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
        test_m = range(30, 200, 5)
    elif args.ultrasonicranger == '2':
        topic = ultrasonic_ranger2_topic
        test_m = range(200, 30, -5)

    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(mqtt_broker_hostname, mqtt_broker_port, keepalive=60)
    # have paho.mqtt spawn a background thread for us
    client.loop_start()

    i = 0
    while True:
        if TEST:
            distance = test_m[i] + random.randint(-5, 5)
            i = (i + 1) % len(test_m)
            time.sleep(0.2)
        else:
            distance = mcp.read_adc(0) 
            time.sleep(0.2)

        print("topic: " + topic + ", distance (cm): " + str(distance))
        client.publish(topic, distance)
