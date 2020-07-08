from datetime import datetime


def calculate_speed(miles_driven, time_in_seconds):
    """
    Calculates the speed given the miles and time

    :param miles_driven: Float
    :param time_in_seconds: Float
    :return: sped: float
    """
    seconds_per_hour = 3600
    time_in_hour = time_in_seconds / seconds_per_hour
    miles_per_hour = 0
    if time_in_hour > 0:
        miles_per_hour = miles_driven / time_in_hour
    return miles_per_hour


class Trip:
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
        self._time_driven = (end_date - start_date).total_seconds()

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
        Return the time driven in seconds

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
