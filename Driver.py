from Trip.Trips import Trips


class Driver:
    def __init__(self):
        self._trips = Trips()

    def add_trip(self, *args):
        self._trips.add_trip(*args)

    @property
    def trips(self):
        """
        Return the trips object that belongs to the driver

        :return: tips: trips object
        """
        return self._trips
