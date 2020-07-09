from Driver.Driver import Driver


class Drivers(dict):
    def add_driver(self, name):
        """
        Adds the name of the driver as the key and the Driver object as the value

        :param name: the name of the driver
        """
        self.update({name: Driver()})

    def add_trip(self, name, *args):
        """
        Adds a trip to the driver object
        :param name: the name of the driver
        :param args: an array of parameters that will be passed down to the
                     trip class. typical includes start_time, end_time,
                     distance_driven
        """
        self[name].add_trip(*args)

    def sort_total_miles_driven(self):
        """
        Sorts the keys by the total_miles_driven connect to the driver

        :return: sorted_keys: an array that has the keys sorted
        """
        return sorted(self, key=lambda x: self[x].get_trip_total_miles_driven(), reverse=True)

    def __str__(self):
        """
        Returns driver as a formatted string

        :return: string
        """
        result = []
        sorted_driver_key = self.sort_total_miles_driven()
        for driver in sorted_driver_key:
            distance = round(self[driver].get_trip_total_miles_driven())
            driver_results = [f"{driver}: {distance} miles"]
            if distance > 0:
                speed = round(self[driver].get_trip_total_average_speed())
                driver_results.append(f"{speed} mph")
            result.append(" ".join(driver_results))
        return "\n".join(result)
