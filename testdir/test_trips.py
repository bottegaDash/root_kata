from Trip import Trip
import unittest

class TestTrip(unittest.TestCase):
    def test_distance(self):
        trip = Trip("00:00", "00:00", "100")
        self.assertEqual(trip.distance, 100)

if __name__ == '__main__':
    unittest.main()