# -*- coding: utf-8 -*-
from .models import SensorData


def get_devices_with_sensors(sensors):
    """
    Get devices with sensors data

    :param sensors: Dict of sensors
    {
        name: {
            start_timestamp
            end_timestamp
            devices
        }
    }

    :return: Dict of devices with sensors data
    {
        mac: [SensorData]
    }
    """
    devices = {}

    for sensor_name in sensors:
        for device in sensors[sensor_name]['devices']:

            sensor_data = SensorData(
                sensor_name,
                sensors[sensor_name]['start_timestamp'],
                sensors[sensor_name]['end_timestamp'],
                device['rssi']
            )

            if device['mac'] not in devices:
                devices[device['mac']] = [sensor_data]

            elif sensor_data not in devices[device['mac']]:
                devices[device['mac']].append(sensor_data)

    return devices


def get_sensors_with_timestamp_intersection(sensors, threshold):
    intersections = []

    # Find possibles groups
    for first_sensor in sensors:

        group = [first_sensor['name']]

        for second_sensor in sensors:

            if (first_sensor['start_timestamp'] + threshold >= second_sensor['end_timestamp']) or (
                    first_sensor['end_timestamp'] - threshold <= second_sensor['start_timestamp']):
                group.append(second_sensor)

        intersections.append(group)

    # Clean

