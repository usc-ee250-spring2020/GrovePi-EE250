import paho.mqtt.client as mqtt
import time

# set to 1 to enable debugging print statements
DEBUG = 0

# MQTT variables
broker_hostname = ''
broker_port = 1883
ultrasonic_ranger1_topic = "ultrasonic_ranger1"
ultrasonic_ranger2_topic = "ultrasonic_ranger2"

# Lists holding the ultrasonic ranger sensor distance readings. Change the 
# value of MAX_LIST_LENGTH depending on how many distance samples you would 
# like to keep at any point in time.
MAX_LIST_LENGTH = 100
ranger1_dist = []
ranger2_dist = []


def ranger1_callback(client, userdata, message):
    ranger1_dist.append(int(msg.payload))
    #truncate list to only have the last MAX_LIST_LENGTH values
    ranger1_dist = ranger1_dist[-MAX_LIST_LENGTH:]

def ranger2_callback(client, userdata, message):
    ranger2_dist.append(int(msg.payload))
    #truncate list to only have the last MAX_LIST_LENGTH values
    ranger2_dist = ranger2_dist[-MAX_LIST_LENGTH:]

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(ultrasonic_ranger1_topic)
    client.message_callback_add(ultrasonic_ranger1_topic, ranger1_callback)
    client.subscribe(ultrasonic_ranger2_topic)
    client.message_callback_add(ultrasonic_ranger2_topic, ranger2_callback)

# The callback for when a PUBLISH message is received from the server.
# This should not be called.
def on_message(client, userdata, msg): 
    print(msg.topic + " " + str(msg.payload))

# Connect to broker and start loop    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
if broker_name == '':
    print "Change the broker address"
    exit()
client.connect(broker_name, broker_port, 60)
client.loop_start()

while True:
    
    # You have two lists (ranger1_dist and ranger2_dist), which are your two signals
    # The signals are published with interval of 200 ms (5 samples per second each signal)
    # The values are the distance in cm to the closest object. Expect values between 0 and 512
    
    # TO-DO - Detect when a person pass by and what direction he/she is going
    
    time.sleep(0.01)