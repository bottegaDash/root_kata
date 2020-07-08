from Trip.Trips import Trips


class Driver:
    def __init__(self):
        self._trips = Trips()

    @property
    def trips(self):
        return self._trips
