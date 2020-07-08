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


if __name__ == '__main__':
    unittest.main()
