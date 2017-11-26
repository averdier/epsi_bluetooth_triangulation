# -*- coding: utf-8 -*-
import json


class Sensor:

    def __init__(self, name, pos, max_radius, max_rssi):
        self._name = name
        self._pos = pos
        self._max_radius = max_radius
        self._max_rssi = max_rssi
        self._data = []

    @property
    def name(self): return self._name

    @property
    def pos(self): return self._pos

    @property
    def data(self): return self._data

    @property
    def max_radius(self): return self._max_radius

    @property
    def max_rssi(self): return self._max_rssi

    def update(self, update_data):
        self._data = []
        try:
            data = json.loads(update_data)
            print(update_data)
            for device in data['devices']:
                self._data.append(SensorData(
                    self,
                    data['start_timestamp'],
                    data['end_timestamp'],
                    device['mac'],
                    device['rssi']
                ))
        except Exception as ex:
            print(ex)

    def __eq__(self, other):
        return self.name == other.name


class SensorData:

    def __init__(self, sensor, start_timestamp, end_timestamp, device_address, rssi):
        self._sensor = sensor
        self._start_timestamp = start_timestamp
        self._end_timestamp = end_timestamp
        self._device_address = device_address
        self._rssi = rssi

    @property
    def sensor(self): return self._sensor

    @property
    def start_timestamp(self): return self._start_timestamp

    @property
    def end_timestamp(self): return self._end_timestamp

    @property
    def device_address(self): return self._device_address

    @property
    def rssi(self): return self._rssi

    def __eq__(self, other):
        return self.sensor == other.sensor \
               and self.start_timestamp == other.start_timestamp \
               and self.end_timestamp == other.end_timestamp \
               and self.device_address == other.device_address \
               and self.rssi == other.rssi
