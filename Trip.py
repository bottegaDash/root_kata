class Trip:
    def __init__(self, start_time, end_time, miles_driven):
        """
        The initialization of a Trip Object
        :param start_time: String: format "00:00"
        :param end_time: String: format "00:00"
        :param miles_driven: String: format "1.0"
        """
        self._miles_driven = float(miles_driven)

    @property
    def miles_driven(self):
        """
        Return the miles_driven of the trip

        :return: miles_driven: Float
        """
        return self._miles_driven
