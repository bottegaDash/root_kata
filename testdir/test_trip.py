from Trip.Trip import Trip
import unittest
from unittest.mock import patch


@patch("Trip.calculate_speed")
class TestTrip(unittest.TestCase):
    def test_miles_driven(self, mock_calculate_speed):
        trip = Trip("00:00", "00:00", "100")
        expected_miles_driven = 100
        actual_miles_driven = trip.miles_driven
        self.assertEqual(expected_miles_driven, actual_miles_driven)

    def test_time_driven(self, mock_calculate_speed):
        trip = Trip("06:12", "06:32", "100")
        expected_time_driven = 1200
        actual_time_driven = trip.time_driven
        self.assertEqual(expected_time_driven, actual_time_driven)

    def test_average_speed(self, mock_calculate_speed):
        mock_calculate_speed.return_value = 60
        trip = Trip("06:12", "06:32", "20")
        expected_average_speed = 60
        actual_average_speed = trip.average_speed
        self.assertEqual(expected_average_speed, actual_average_speed)

    def test_is_valid(self, mock_calculate_speed):
        mock_calculate_speed.return_value = 20
        trip = Trip("06:12", "06:32", "20")
        expected_is_valid = True
        actual_is_valid = trip.is_valid
        self.assertEqual(expected_is_valid, actual_is_valid)

    def test_is_not_valid_below_lower_bound(self, mock_calculate_speed):
        mock_calculate_speed.return_value = 4
        trip = Trip("07:00", "08:00", "6")
        expected_is_valid = False
        actual_is_valid = trip.is_valid
        self.assertEqual(expected_is_valid, actual_is_valid)

    def test_is_not_valid_above_upper_bound(self, mock_calculate_speed):
        mock_calculate_speed.return_value = 101
        trip = Trip("07:00", "08:00", "6")
        expected_is_valid = False
        actual_is_valid = trip.is_valid
        self.assertEqual(expected_is_valid, actual_is_valid)


if __name__ == '__main__':
    unittest.main()
