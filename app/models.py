# -*- coding: utf-8 -*-


class SensorData:

    def __init__(self, sensor_name, start_timestamp, end_timestamp, device_address):
        self._sensor_name = sensor_name
        self._start_timestamp = start_timestamp
        self._end_timestamp = end_timestamp
        self._device_address = device_address

    @property
    def sensor_name(self): return self.sensor_name

    @property
    def start_timestamp(self): return self._start_timestamp

    @property
    def end_timestamp(self): return self._end_timestamp

    @property
    def device_address(self): return self._device_address

    def __eq__(self, other):
        return self.sensor_name == other.sensor_name \
               and self.start_timestamp == other.start_timestamp \
               and self.end_timestamp == other.end_timestamp \
               and self.device_address == other.device_address
