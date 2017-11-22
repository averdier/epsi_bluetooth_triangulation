# -*- coding: utf-8 -*-

import sys
import paho.mqtt.client as ns_client


mqtt_username = 'triangulation_service'
mqtt_key = ''
mqtt_server_address = 'localhost'
mqtt_port = 1883
mqtt_keep_alive = 60

topics = [
    'sensor/device_01/from_device',
    'sensor/device_02/from_device',
    'sensor/device_03/from_device',
]


mqtt = ns_client.Client()


def on_connect(client, userdata, flags, rc):
    print('Connection result code: ' + str(rc))

    if rc == 4:
        print('Invalid credentials')
        sys.exit(1)

    for topic in topics:
        client.subscribe(topic)


def on_message(client, userdata, msg):

    if msg.topic == topics[0]:
        pass

    elif msg.topic == topics[1]:
        pass

    elif msg.topic == topics[2]:
        pass


if __name__ == '__main__':
    mqtt.username_pw_set(mqtt_username, mqtt_key)
    mqtt.on_connect = on_connect
    mqtt.on_message = on_message

    mqtt.connect(mqtt_server_address, mqtt_port, mqtt_keep_alive)

    mqtt.loop_forever()



