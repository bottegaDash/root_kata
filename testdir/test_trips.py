from Driver.Trip.Trips import Trips
import unittest
from unittest.mock import patch, PropertyMock


class TestTrip(unittest.TestCase):
    def test_get_trips(self):
        trips = Trips()
        expected_trips = []
        actual_trips = trips.trips
        self.assertEqual(expected_trips, actual_trips)

    @patch("Driver.Trip.Trips.Trip")
    @patch("Driver.Trip.Trips.calculate_speed")
    def test_add_trip_calls_trip(self, mock_calculate_speed, mock_trip):
        type(mock_trip.return_value).is_valid = PropertyMock(return_value=True)
        mock_calculate_speed.return_value = 60
        trips = Trips()
        trips.add_trip("00:00", "01:00", "10")
        self.assertEqual(mock_trip.call_args[0], ("00:00", "01:00", "10"))

    @patch("Driver.Trip.Trips.Trip")
    @patch("Driver.Trip.Trips.calculate_speed")
    def test_add_trip_to_array(self, mock_calculate_speed, mock_trip):
        type(mock_trip.return_value).is_valid = PropertyMock(return_value=True)
        mock_calculate_speed.return_value = 60
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

    @patch("Driver.Trip.Trips.Trip")
    @patch("Driver.Trip.Trips.calculate_speed")
    def test_add_total_miles_driven(self, mock_calculate_speed, mock_trip):
        type(mock_trip.return_value).is_valid = PropertyMock(return_value=True)
        mock_calculate_speed.return_value = 60
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

    @patch("Driver.Trip.Trips.Trip")
    @patch("Driver.Trip.Trips.calculate_speed")
    def test_add_total_time_driven(self, mock_calculate_speed, mock_trip):
        type(mock_trip.return_value).is_valid = PropertyMock(return_value=True)
        mock_calculate_speed.return_value = 60
        type(mock_trip.return_value).time_driven = PropertyMock(return_value=360)
        trips = Trips()
        trips.add_trip("00:00", "01:00", "39")
        expected_total_time_driven = 360
        actual_total_time_driven = trips.total_time_driven
        self.assertEqual(expected_total_time_driven, actual_total_time_driven)

    def test_get_total_average_speed(self):
        trips = Trips()
        expected_total_average_speed = 0
        actual_total_average_speed = trips.total_average_speed
        self.assertEqual(expected_total_average_speed, actual_total_average_speed)

    @patch("Driver.Trip.Trips.Trip")
    @patch("Driver.Trip.Trips.calculate_speed")
    def test_calling_calculate_speed(self, mock_calculate_speed, mock_trip):
        type(mock_trip.return_value).time_driven = PropertyMock(return_value=1800)
        type(mock_trip.return_value).miles_driven = PropertyMock(return_value=60)
        trips = Trips()
        trips.add_trip("00:00", "00:30", "30")
        mock_calculate_speed.assert_called_with(60, 1800)

    @patch("Driver.Trip.Trips.Trip")
    @patch("Driver.Trip.Trips.calculate_speed")
    def test_updating_total_speed(self, mock_calculate_speed, mock_trip):
        type(mock_trip.return_value).time_driven = PropertyMock(return_value=1800)
        type(mock_trip.return_value).miles_driven = PropertyMock(return_value=60)
        mock_calculate_speed.return_value = 60
        trips = Trips()
        trips.add_trip("00:00", "00:30", "30")
        expected_total_speed = 60
        actual_total_speed = trips.total_average_speed
        self.assertEqual(expected_total_speed, actual_total_speed)

    @patch("Driver.Trip.Trips.Trip")
    def test_dropping_invalid_trip(self, mock_trip):
        type(mock_trip.return_value).is_valid = PropertyMock(return_value=False)
        trips = Trips()
        trips.add_trip("00:00", "01:00", "10")
        expected_trips_length = 0
        actual_trips_length = len(trips.trips)
        self.assertEqual(expected_trips_length, actual_trips_length)


if __name__ == '__main__':
    unittest.main()