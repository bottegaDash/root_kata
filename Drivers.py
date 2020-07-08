from Driver import Driver


class Drivers(dict):
    def add_driver(self, name):
        self.update({name: Driver()})