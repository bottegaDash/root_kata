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

if __name__ == '__main__':
    unittest.main()