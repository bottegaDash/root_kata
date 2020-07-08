import unittest
from unittest.mock import patch, Mock, PropertyMock, MagicMock
from Drivers import Drivers

class TestTrip(unittest.TestCase):

    @patch("Drivers.Driver")
    def test_add_driver(self, mock_driver):
        actual_drivers = Drivers()
        actual_drivers.add_driver("Apple")
        expected_drivers = {"Apple": mock_driver()}
        self.assertEqual(expected_drivers, actual_drivers)

    @patch("Drivers.Driver")
    def test_add_trip(self, mock_driver):
        drivers = Drivers()
        drivers.add_driver("Apple")
        drivers.add_trip("Apple", "00:00", "01:00", "60")
        self.assertEqual(mock_driver().add_trip.call_args[0], ("00:00", "01:00", "60"))

    @patch("Drivers.Driver")
    def test_sort_total_miles_driven(self, mock_driver):
        drivers = Drivers()
        mock_driver().get_total_miles_driven.side_effect = [5, 8, 3, 4]
        drivers.add_driver("driver_5")
        drivers.add_driver("driver_8")
        drivers.add_driver("driver_3")
        drivers.add_driver("driver_4")
        expected_sort_distance = ["driver_8", "driver_5", "driver_4", "driver_3"]
        actual_sort_distance = drivers.sort_total_miles_driven()
        self.assertEqual(expected_sort_distance, actual_sort_distance)


if __name__ == '__main__':
    unittest.main()