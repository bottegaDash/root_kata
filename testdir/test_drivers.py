import unittest
from unittest.mock import patch
from Drivers import Drivers


@patch("Drivers.Driver")
class TestTrip(unittest.TestCase):

    def test_add_driver(self, mock_driver):
        actual_drivers = Drivers()
        actual_drivers.add_driver("Apple")
        expected_drivers = {"Apple": mock_driver()}
        self.assertEqual(expected_drivers, actual_drivers)

    def test_add_trip(self, mock_driver):
        drivers = Drivers()
        drivers.add_driver("Apple")
        drivers.add_trip("Apple", "00:00", "01:00", "60")
        self.assertEqual(mock_driver().add_trip.call_args[0], ("00:00", "01:00", "60"))

    def test_sort_total_miles_driven(self, mock_driver):
        drivers = Drivers()
        mock_driver().get_trip_total_miles_driven.side_effect = [5, 8, 3, 4]
        drivers.add_driver("driver_5")
        drivers.add_driver("driver_8")
        drivers.add_driver("driver_3")
        drivers.add_driver("driver_4")
        expected_sort_distance = ["driver_8", "driver_5", "driver_4", "driver_3"]
        actual_sort_distance = drivers.sort_total_miles_driven()
        self.assertEqual(expected_sort_distance, actual_sort_distance)

    def test_print_drivers(self, mock_driver):
        drivers = Drivers()
        mock_driver().get_trip_total_miles_driven.side_effect = [5, 0, 5, 0]
        mock_driver().get_trip_total_average_speed.side_effect = [20]
        drivers.add_driver("Person1")
        drivers.add_driver("Person2")
        expected_driver_string = "Person1: 5 miles 20 mph\nPerson2: 0 miles"
        actual_driver_string = str(drivers)
        self.assertEqual(expected_driver_string, actual_driver_string)


if __name__ == '__main__':
    unittest.main()