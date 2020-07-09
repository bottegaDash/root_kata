from Trip.Trips import Trips


class Driver:
    def __init__(self):
        self._trips = Trips()

    def add_trip(self, *args):
        """
        Calls the add_trip method in Trips
        :param args: an array of parameters that will be passed down to the
                     trip class. typical includes start_time, end_time,
                     distance_driven
        """
        self._trips.add_trip(*args)

    def get_trip_total_miles_driven(self):
        """
        gets the total miles driven of the trip

        :return: total_miles_driven: Float
        """
        return self._trips.total_miles_driven

    def get_trip_total_time_driven(self):
        """
        gets the total time driven of the trip

        :return: total_time_driven: Float in hours
        """
        return self._trips.total_time_driven

    def get_trip_total_average_speed(self):
        """
        get the total average speed
        :return: total_average_speed: Float in miles per hour
        """
        return self._trips.total_average_speed

    @property
    def trips(self):
        """
        Return the trips object that belongs to the driver

        :return: tips: trips object
        """
        return self._trips
