import unittest
from unittest.mock import patch, mock_open
from Parser import parse_input


@patch("Parser.Drivers")
class TestDriver(unittest.TestCase):

    def test_add_driver(self, mock_drivers):
        m = mock_open(read_data="Driver Adam")
        with patch('builtins.open', m):
            parse_input("/a/b/c")
            mock_drivers().add_driver.assert_called_with("Adam")

    def test_add_trip(self, mock_drivers):
        m = mock_open(read_data="""Driver Adam\n
                                   Trip Adam 00:00 01:00 60""")
        with patch('builtins.open', m):
            parse_input("/a/b/c")
            mock_drivers().add_trip.assert_called_with("Adam", "00:00", "01:00", "60")

    def test_get_driver_object(self, mock_drivers):
        m = mock_open(read_data="")
        with patch('builtins.open', m):
            driver_object = parse_input("/a/b/c")
            self.assertEqual(driver_object, mock_drivers())


if __name__ == '__main__':
    unittest.main()