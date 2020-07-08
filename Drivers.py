from Driver import Driver


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
