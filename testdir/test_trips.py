from Trip import Trip, calculate_speed
import unittest


class TestTrip(unittest.TestCase):
    def test_miles_driven(self):
        trip = Trip("00:00", "00:00", "100")
        expected_miles_driven = 100
        actual_miles_driven = trip.miles_driven
        self.assertEqual(expected_miles_driven, actual_miles_driven)

    def test_time_driven(self):
        trip = Trip("06:12", "06:32", "100")
        expected_time_driven = 1200
        actual_time_driven = trip.time_driven
        self.assertEqual(expected_time_driven, actual_time_driven)

    def test_calculate_speed(self):
        miles_driven = 20
        time_in_seconds = 1200
        expected_calculated_speed = 60
        actual_calculated_speed = calculate_speed(miles_driven, time_in_seconds)
        self.assertEqual(expected_calculated_speed, actual_calculated_speed)

    def test_calculate_speed_with_time_as_zero(self):
        miles_driven = 20
        time_in_seconds = 0
        expected_calculated_speed = 0
        actual_calculated_speed = calculate_speed(miles_driven, time_in_seconds)
        self.assertEqual(expected_calculated_speed, actual_calculated_speed)

    def test_average_speed(self):
        trip = Trip("06:12", "06:32", "20")
        expected_average_speed = 60
        actual_average_speed = trip.average_speed
        self.assertEqual(expected_average_speed, actual_average_speed)

    def test_is_valid(self):
        trip = Trip("06:12", "06:32", "20")
        expected_is_valid = True
        actual_is_valid = trip.is_valid
        self.assertEqual(expected_is_valid, actual_is_valid)

    def test_is_not_valid_below_lower_bound(self):
        trip = Trip("07:00", "08:00", "4")
        expected_is_valid = False
        actual_is_valid = trip.is_valid
        self.assertEqual(expected_is_valid, actual_is_valid)


if __name__ == '__main__':
    unittest.main()
