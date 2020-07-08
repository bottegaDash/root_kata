class Trip:
    def __init__(self, start_time, end_time, distance):
        """
        The initialization of a Trip Object
        :param start_time: String: format "00:00"
        :param end_time: String: format "00:00"
        :param distance: String: format "1.0"
        """
        self._distance = float(distance)


    @property
    def distance(self):
        """
        Return the distance of the trip

        :return: distance: Float
        """
        return self._distance
