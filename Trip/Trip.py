from Trip.trip_helper import calculate_speed
from datetime import datetime


class Trip:

    LOWER_SPEED_BOUNDARY = 5.0
    UPPER_SPEED_BOUNDARY = 100.0

    def __init__(self, start_time, end_time, miles_driven):
        """
        The initialization of a Trip Object
        :param start_time: String: format "00:00"
        :param end_time: String: format "00:00"
        :param miles_driven: String: format "1.0"
        """
        self._miles_driven = float(miles_driven)

        start_date = datetime.strptime(start_time, '%H:%M')
        end_date = datetime.strptime(end_time, '%H:%M')
        seconds_per_hour = 3600
        self._time_driven = (end_date - start_date).total_seconds() / seconds_per_hour

        self._average_speed = calculate_speed(self._miles_driven, self._time_driven)

    @property
    def miles_driven(self):
        """
        Return the miles_driven of the trip

        :return: miles_driven: Float
        """
        return self._miles_driven

    @property
    def time_driven(self):
        """
        Return the time driven in hours

        :return: time_driven: Float
        """
        return self._time_driven

    @property
    def average_speed(self):
        """
        Return the average speed of the trip in mph

        :return: average_speed: Float
        """
        return self._average_speed

    @property
    def is_valid(self):
        """
        Returns boolean stating if trip is valid

        :return: is_valid: boolean
        """
        return self.LOWER_SPEED_BOUNDARY <= self._average_speed <= self.UPPER_SPEED_BOUNDARY
