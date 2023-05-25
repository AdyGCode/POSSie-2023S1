# Demonstration MQTT Publisher & Subscriber
#
# Filename:     subscriber.py
# Author:       Adrian Gould
#
# Purpose:      This file demonstrates how to subscribe to
#               a MQTT topic on a Mosquitto Server running
#               on the local computer (localhost).

# import paho mqtt client, aliased as mqtt
import paho.mqtt.client as mqtt
from datetime import datetime
import json

# Create the settings for our Subscriber
MQTT_HOST = "localhost"   # replace localhost with the computer name that MQTT is running on
MQTT_PORT = 1883  # default MQTT port
MQTT_KEEP_ALIVE = 300  # seconds - this keeps the connection "open"

MQTT_CLIENT_NAME = "duck-on"  # Should (MUST) be unique!
MQTT_TOPIC_ONE = "test/ducks"  # main topic: test, subtopic: ducks
MQTT_TOPIC_TWO = "test/geese"  # main topic: test, subtopic: ducks

topics = [MQTT_TOPIC_ONE, MQTT_TOPIC_TWO]

# Instantiate an MQTT Client
client = mqtt.Client(MQTT_CLIENT_NAME)
# connect to the server/broker
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)

# subscribe to the topics
for topic in topics:
    client.subscribe(topic)


def on_message_callback(client, userdata, message):
    msg = message
    # decode the message payload into UTF-8 characters
    msg_data = str(msg.payload.decode("UTF-8"))
    data = json.loads(msg_data)

    print(f"{data}")
    print(f"Topic: {msg.topic} QoS: {msg.qos} Retain: {msg.retain}")

# Listen for messages - call the "callback" when one is received.
client.on_message = on_message_callback

print(f"{MQTT_CLIENT_NAME} is listening on port {MQTT_PORT}")
print(f"subscribed to topics: {topics}")

client.loop_forever()
