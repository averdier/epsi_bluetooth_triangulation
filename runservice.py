# -*- coding: utf-8 -*-

import sys
import json
import paho.mqtt.client as ns_client
from app.models import Sensor
from app.utils import get_devices_with_sensors, group_data_by_match_interval

mqtt_username = 'triangulation_service'
mqtt_key = 'Viyywn1hMyME83yM'
mqtt_server_address = '93.118.34.190'
mqtt_port = 1883
mqtt_keep_alive = 60


sensors = {
    'device_01': Sensor('device_01', [10, 10], 4000, -90),
    'device_02': Sensor('device_02', [10, 10], 4000, -90),
    'device_03': Sensor('device_03', [10, 10], 4000, -90)
}

mqtt = ns_client.Client()


def on_sensor_update():

    devices = get_devices_with_sensors(list(sensors.values()))

    for device_address in devices:
        groups = group_data_by_match_interval(devices[device_address])

        print('groups: {0}'.format(groups))


def on_connect(client, userdata, flags, rc):
    print('Connection result code: ' + str(rc))

    if rc == 4:
        print('Invalid credentials')
        sys.exit(1)

    for sensor_name in sensors:
        client.subscribe('sensor/' + sensor_name + '/from_device')


def on_message(client, userdata, msg):

    topic_parts = msg.topic.split('/')

    if len(topic_parts) == 3 and sensors.get(topic_parts[1], None) is not None and topic_parts[2] == 'from_device':
        print('Update from ' + topic_parts[1])
        sensors[topic_parts[1]].update(msg.payload.decode('utf-8'))
        on_sensor_update()


if __name__ == '__main__':
    mqtt.username_pw_set(mqtt_username, mqtt_key)
    mqtt.on_connect = on_connect
    mqtt.on_message = on_message

    mqtt.connect(mqtt_server_address, mqtt_port, mqtt_keep_alive)

    mqtt.loop_forever()
