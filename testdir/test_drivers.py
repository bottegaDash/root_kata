import unittest
from unittest.mock import patch, Mock, PropertyMock
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


if __name__ == '__main__':
    unittest.main()