from Trips import Trips
import unittest
from unittest.mock import patch, PropertyMock


class TestTrip(unittest.TestCase):
    def test_get_trips(self):
        trips = Trips()
        expected_trips = []
        actual_trips = trips.trips
        self.assertEqual(expected_trips, actual_trips)

    @patch("Trips.Trip")
    def test_add_trip_calls_trip(self, mock_trip):
        trips = Trips()
        trips.add_trip("00:00", "01:00", "10")
        self.assertEqual(mock_trip.call_args[0], ("00:00", "01:00", "10"))

    @patch("Trips.Trip")
    def test_add_trip_to_array(self, mock_trip):
        trips = Trips()
        trips.add_trip("00:00", "01:00", "10")
        expected_trips_length = 1
        actual_trips_length = len(trips.trips)
        self.assertEqual(expected_trips_length, actual_trips_length)

    def test_get_total_miles_driven(self):
        trips = Trips()
        expected_total_miles_driven = 0
        actual_total_miles_driven = trips.total_miles_driven
        self.assertEqual(expected_total_miles_driven, actual_total_miles_driven)

    @patch("Trips.Trip")
    def test_add_total_miles_driven(self, mock_trip):
        type(mock_trip.return_value).miles_driven = PropertyMock(return_value=10)
        trips = Trips()
        trips.add_trip("00:00", "01:00", "39")
        expected_total_miles_driven = 10
        actual_total_miles_driven = trips.total_miles_driven
        self.assertEqual(expected_total_miles_driven, actual_total_miles_driven)

    def test_get_total_time_driven(self):
        trips = Trips()
        expected_total_time_driven = 0
        actual_total_time_driven = trips.total_time_driven
        self.assertEqual(expected_total_time_driven, actual_total_time_driven)

    @patch("Trips.Trip")
    def test_add_total_time_driven(self, mock_trip):
        type(mock_trip.return_value).time_driven = PropertyMock(return_value=360)
        trips = Trips()
        trips.add_trip("00:00", "01:00", "39")
        expected_total_time_driven = 360
        actual_total_time_driven = trips.total_time_driven
        self.assertEqual(expected_total_time_driven, actual_total_time_driven)


if __name__ == '__main__':
    unittest.main()