from Trip import Trip
from Trip.trip_helper import calculate_speed


class Trips:
    def __init__(self):
        self._trips = []
        self._total_miles_driven = 0
        self._total_time_driven = 0
        self._total_average_speed = 0

    @property
    def trips(self):
        """
        Return an array of trip

        :return: trips: Array of trip
        """
        return self._trips

    def add_trip(self, *args):
        trip = Trip(*args)
        if trip.is_valid:
            self._trips.append(trip)
            self._total_miles_driven += trip.miles_driven
            self._total_time_driven += trip.time_driven
            self._total_average_speed = calculate_speed(self._total_miles_driven, self._total_time_driven)


    @property
    def total_miles_driven(self):
        """
        Returns the sum of total miles driver

        :return: total_miles_driven: float
        """
        return self._total_miles_driven

    @property
    def total_time_driven(self):
        """
        Returns the sum of total time driver

        :return: total_time_driven: float in seconds
        """
        return self._total_time_driven

    @property
    def total_average_speed(self):
        """
        Returns the overall average speed

        :return: total_average_speed: float in miles per hour
        """
        return self._total_average_speed
