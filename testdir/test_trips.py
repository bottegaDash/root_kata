from Trip import Trip
import unittest


class TestTrip(unittest.TestCase):
    def test_miles_driven(self):
        trip = Trip("00:00", "00:00", "100")
        self.assertEqual(trip.miles_driven, 100)

    def test_time_driven(self):
        trip = Trip("06:12", "06:32", "100")
        self.assertEqual(trip.time_driven, 1200)


if __name__ == '__main__':
    unittest.main()
