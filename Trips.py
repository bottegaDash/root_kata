from Trip import Trip


class Trips:
    def __init__(self):
        self._trips = []
        self._total_miles_driven = 0

    @property
    def trips(self):
        """
        Return an array of trip

        :return: trips: Array of trip
        """
        return self._trips

    def add_trip(self, *args):
        trip = Trip(*args)
        self._trips.append(trip)

    @property
    def total_miles_driven(self):
        """
        Returns the sum of total miles driver

        :return: total_miles_driven: float
        """
        return self._total_miles_driven
