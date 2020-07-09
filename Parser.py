from Driver.Drivers import Drivers


def parse_input(input_file):
    """
    Takes in a file and builds a drivers_object based on the commands and parameters
    passed through

    :param input_file: the file to parse
    :return: drives_object: the drivers_object
    """
    drivers_object = Drivers()
    with open(input_file) as fp:
        for line in fp:
            line = line.strip()
            command = line.split(' ')[0]
            parameters = line.split(' ')[1:]
            if command == "Driver":
                drivers_object.add_driver(*parameters)
            elif command == "Trip":
                drivers_object.add_trip(*parameters)
    return drivers_object
