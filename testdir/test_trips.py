from Trips import Trips
import unittest
from unittest.mock import patch


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


if __name__ == '__main__':
    unittest.main()