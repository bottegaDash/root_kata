import unittest
from unittest.mock import patch, Mock, PropertyMock
from Driver.Driver import Driver


@patch("Driver.Driver.Trips")
class TestDriver(unittest.TestCase):

    def test_get_trips(self, mock_trips):
        driver = Driver()
        expected_driver_trips_type = mock_trips()
        actual_driver_trips_type = driver.trips
        self.assertEqual(expected_driver_trips_type, actual_driver_trips_type)

    def test_add_trip(self, mock_trips):
        driver = Driver()
        mock_trips.add_trip = Mock()
        driver.add_trip()
        mock_trips().add_trip.assert_called_once()

    def test_get_trip_total_miles_driven(self, mock_trips):
        driver = Driver()
        type(mock_trips.return_value).total_miles_driven = PropertyMock(return_value=10)
        expected_total_miles_driven = 10
        actual_total_miles_driven = driver.get_trip_total_miles_driven()
        self.assertEqual(expected_total_miles_driven, actual_total_miles_driven)

    def test_get_trip_total_time_driven(self, mock_trips):
        driver = Driver()
        type(mock_trips.return_value).total_time_driven = PropertyMock(return_value=0.44)
        expected_total_time_driven = 0.44
        actual_total_time_driven = driver.get_trip_total_time_driven()
        self.assertEqual(expected_total_time_driven, actual_total_time_driven)

    def test_get_trip_total_average_speed(self, mock_trips):
        driver = Driver()
        type(mock_trips.return_value).total_average_speed = PropertyMock(return_value=0.02)
        expected_total_average_speed = 0.02
        actual_total_average_speed = driver.get_trip_total_average_speed()
        self.assertEqual(expected_total_average_speed, actual_total_average_speed)


if __name__ == '__main__':
    unittest.main()
