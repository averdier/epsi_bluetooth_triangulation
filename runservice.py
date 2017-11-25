# -*- coding: utf-8 -*-

import sys
import json
import paho.mqtt.client as ns_client

mqtt_username = 'triangulation_service'
mqtt_key = 'Viyywn1hMyME83yM'
mqtt_server_address = '93.118.34.190'
mqtt_port = 1883
mqtt_keep_alive = 60

topics = [
    'sensor/device_01/from_device',
    'sensor/device_02/from_device',
    'sensor/device_03/from_device',
]

sondes = {}

mqtt = ns_client.Client()


def show_sondes():
    print(json.dumps(sondes, indent=4))


def get_sondes_where_is_device(device):
    founded_sondes = []

    for sonde in sondes:
        for device in sondes[sonde]['devices']:
            if device['mac'] == device['mac']:

                sonde_already_exist = False

                for s in founded_sondes:
                    if s.get(sonde, None) is not None:
                        sonde_already_exist = True

                if not sonde_already_exist:
                    founded_sondes.append({
                        sonde: {
                            'start_timestamp': sondes[sonde]['start_timestamp'],
                            'end_timestamp': sondes[sonde]['end_timestamp'],
                            'rssi': device['rssi']
                        }
                    })

    return founded_sondes


def get_intersect_sondes(founded_sondes):
    inserect_sondes = []

    for sonde in founded_sondes:
        for s2 in founded_sondes:
            pass


def get_candidates_devices():
    candidates = {}

    for sonde in sondes:
        for device in sondes[sonde]['devices']:

            if candidates.get(device['mac'], None) is None:
                founded_sondes = get_sondes_where_is_device(device)

                if len(founded_sondes) >= 3:
                    candidates[device['mac']] = founded_sondes

    return candidates


def on_connect(client, userdata, flags, rc):
    print('Connection result code: ' + str(rc))

    if rc == 4:
        print('Invalid credentials')
        sys.exit(1)

    for topic in topics:
        client.subscribe(topic)


def on_message(client, userdata, msg):
    if msg.topic == topics[0]:
        data = json.loads(msg.payload.decode('utf-8'))
        sondes['device_01'] = data
        print('Update from device_01')

    elif msg.topic == topics[1]:
        data = json.loads(msg.payload.decode('utf-8'))
        sondes['device_02'] = data
        print('Update from device_02')

    elif msg.topic == topics[2]:
        data = json.loads(msg.payload.decode('utf-8'))
        sondes['device_03'] = data

    candidates = get_candidates_devices()

    print('Candidates')
    print(json.dumps(candidates, 4))


if __name__ == '__main__':
    mqtt.username_pw_set(mqtt_username, mqtt_key)
    mqtt.on_connect = on_connect
    mqtt.on_message = on_message

    mqtt.connect(mqtt_server_address, mqtt_port, mqtt_keep_alive)

    mqtt.loop_forever()
