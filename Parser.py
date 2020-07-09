from Drivers import Drivers


def parse_input(input_file):
    d = Drivers()
    with open(input_file) as fp:
        for line in fp:
            line = line.strip()
            parameters = line.split(' ')[1:]
            d.add_driver(*parameters)
