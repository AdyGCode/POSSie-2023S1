# Demonstration MQTT Publisher & Subscriber
#
# Filename:     subscriber.py
# Author:       Adrian Gould
#
# Purpose:      This file demonstrates how to publish data to
#               a MQTT topic on a Mosquitto Server running
#               on the local computer (localhost).


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

message_to_send = "Hello..."

client.publish(MQTT_TOPIC, message_to_send)
