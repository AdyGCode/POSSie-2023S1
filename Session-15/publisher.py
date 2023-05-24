# Demonstration MQTT Publisher & Subscriber
#
# Filename:     subscriber.py
# Author:       Adrian Gould
#
# Purpose:      This file demonstrates how to publish data to
#               a MQTT topic on a Mosquitto Server running
#               on the local computer (localhost).

import time
from random import randrange, uniform
import json
from datetime import datetime

# import paho mqtt client, aliased as mqtt
import paho.mqtt.client as mqtt

# Create the settings for our Subscriber
MQTT_HOST = "localhost"   # replace localhost with the computer name that MQTT is running on
MQTT_PORT = 1883  # default MQTT port
MQTT_KEEP_ALIVE = 300  # seconds - this keeps the connection "open"

MQTT_CLIENT_NAME = "duck-off"  # Should (MUST) be unique!
MQTT_TOPIC = "test/ducks"  # main topic: test, subtopic: ducks

# Instantiate an MQTT Client
client = mqtt.Client(MQTT_CLIENT_NAME)
# connect to the server/broker
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)

print(f"Sending message to MQTT broker {MQTT_HOST} on port {MQTT_PORT}")
print(f"with the topic {MQTT_TOPIC}...")


while True:
    time.sleep(5)
    temperature = uniform(20, 25)
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ+0800")
    message_data = {
        "client": MQTT_CLIENT_NAME,
        "temp" : temperature,
        "datetime": now
    }
    # convert the dictionary to JSON format
    message_to_send = json.dumps(message_data)
    print(f"Temperature is {temperature} at {now}")
    client.publish(MQTT_TOPIC, message_to_send)
