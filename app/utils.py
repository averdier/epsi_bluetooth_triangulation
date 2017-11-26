# -*- coding: utf-8 -*-
from .models import SensorData


def get_devices_with_sensors(sensors):
    """
    Get devices with sensors data

    :param sensors: List of sensors

    :return: Dict of devices with sensors data
    {
        mac: [SensorData]
    }
    """
    devices = {}

    for sensor in sensors:
        for data in sensor.data:

            if data.device_address not in devices:
                devices[data.device_address] = [data]

            elif data not in devices[data.device_address]:
                devices[data.device_address].append(data)

    return devices


def group_data_by_match_interval(sensor_datas, threshold=5):
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

            if not same_group:
                break

        if not same_group:
            groups.append(first_group)

    return groups

