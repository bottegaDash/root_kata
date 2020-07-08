import unittest
from unittest.mock import patch, Mock, PropertyMock
from Driver import Driver


class TestDriver(unittest.TestCase):

    @patch("Driver.Trips")
    def test_get_trips(self, mock_trips):
        driver = Driver()
        expected_driver_trips_type = mock_trips()
        actual_driver_trips_type = driver.trips
        self.assertEqual(expected_driver_trips_type, actual_driver_trips_type)

    @patch("Driver.Trips")
    def test_add_trip(self, mock_trips):
        driver = Driver()
        mock_trips.add_trip = Mock()
        driver.add_trip()
        mock_trips().add_trip.assert_called_once()

    @patch("Driver.Trips")
    def test_get_trip_total_miles_driven(self, mock_trips):
        driver = Driver()
        mock_trips().total_miles_driven.return_value=10
        expected_total_miles_driven = 10
        actual_total_miles_driven = driver.get_trip_total_miles_driven()
        self.assertEqual(expected_total_miles_driven, actual_total_miles_driven)


if __name__ == '__main__':
    unittest.main()
