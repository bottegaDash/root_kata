from Trip.Trips import Trips


class Driver:
    def __init__(self):
        self._trips = Trips()

    def add_trip(self, *args):
        """
        Calls the add_trip method in Trips
        :param args: an array of parameters that will be passed down to the
                     last class. typical includes start_time, end_time,
                     distance_driven
        """
        self._trips.add_trip(*args)

    @property
    def trips(self):
        """
        Return the trips object that belongs to the driver

        :return: tips: trips object
        """
        return self._trips
