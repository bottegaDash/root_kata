from Trips import Trips
import unittest


class TestTrip(unittest.TestCase):
    def test_get_trips(self):
        trips = Trips()
        expected_trips = []
        actual_trips = trips.trips
        self.assertEqual(expected_trips, actual_trips)


if __name__ == '__main__':
    unittest.main()