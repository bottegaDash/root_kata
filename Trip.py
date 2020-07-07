class Trip:
    def __init__(self, start_time, end_time, distance):
        self._distance = float(distance)

    @property
    def distance(self):
        return self._distance
