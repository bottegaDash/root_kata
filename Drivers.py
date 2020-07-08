from Driver import Driver


class Drivers(dict):
    def add_driver(self, name):
        """
        Adds the name of the driver as the key and the Driver object as the value
        
        :param name: the name of the drive
        """
        self.update({name: Driver()})
