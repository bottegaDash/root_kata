from datetime import datetime


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
