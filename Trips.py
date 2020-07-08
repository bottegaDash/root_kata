from Trip import Trip


class Trips:
    def __init__(self):
        self._trips = []

    @property
    def trips(self):
        """
        Return an array of trip

        :return: trips: Array of trip
        """
        return self._trips

    def add_trip(self, *args):
        Trip(*args)
