from trip_helper import calculate_speed
import unittest


class TestTrip(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()