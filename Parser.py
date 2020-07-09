from Drivers import Drivers


def parse_input(input_file):
    d = Drivers()
    with open(input_file) as fp:
        for line in fp:
            line = line.strip()
            command = line.split(' ')[0]
            parameters = line.split(' ')[1:]
            if command == "Driver":
                d.add_driver(*parameters)
            elif command == "Trip":
                d.add_trip(*parameters)
