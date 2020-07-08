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


if __name__ == '__main__':
    unittest.main()