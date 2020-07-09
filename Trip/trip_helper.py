def calculate_speed(miles_driven, time_in_hours):
    """
    Calculates the speed given the miles and time

    :param miles_driven: Float
    :param time_in_hourss: Float
    :return: sped: float
    """
    miles_per_hour = 0
    if time_in_hours > 0:
        miles_per_hour = miles_driven / time_in_hours
    return miles_per_hour
