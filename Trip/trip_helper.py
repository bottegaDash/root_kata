def calculate_speed(miles_driven, time_in_seconds):
    """
    Calculates the speed given the miles and time

    :param miles_driven: Float
    :param time_in_seconds: Float
    :return: sped: float
    """
    seconds_per_hour = 3600
    time_in_hour = time_in_seconds / seconds_per_hour
    miles_per_hour = 0
    if time_in_hour > 0:
        miles_per_hour = miles_driven / time_in_hour
    return miles_per_hour
