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


def group_data_by_match_interval(sensor_datas, threshold = 5):
    """
    Group list of SensorData by match interval

    :param sensor_datas:
    :param threshold:

    :return: SensorData group by match interval
    [[SensorData]]
    """
    temp_groups = []

    # Find possibles groups
    for first_data in sensor_datas:

        group = [first_data]
        for second_data in sensor_datas:

            if first_data != second_data:
                if (first_data.start_timestamp - threshold <= second_data.end_timestamp) or (
                                first_data.end_timestamp + threshold >= second_data.start_timestamp):
                    group.append(second_data)

        temp_groups.append(group)

    groups = []

    for first_group in temp_groups:

        same_group = True
        for second_group in temp_groups:

            if len(first_group) != len(second_group):
                same_group = False
                break

            for i in range(0, len(first_group)):
                if first_group[i] != second_group[i]:
                    same_group = False
                    break

            if not second_group:
                break

        if not same_group:
            groups.append(first_group)

    return groups

