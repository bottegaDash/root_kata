import unittest
from unittest.mock import patch
from Driver import Driver


class TestTrip(unittest.TestCase):

    @patch("Driver.trips")
    def test_get_trips(self, mock_trips):
        driver = Driver()
        expected_driver_trips_type = mock_trips
        actual_driver_trips_type = driver.trips
        self.assertEqual(expected_driver_trips_type, actual_driver_trips_type)


if __name__ == '__main__':
    unittest.main()
