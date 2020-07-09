import unittest
from unittest.mock import patch, mock_open
from Parser import parse_input


class TestDriver(unittest.TestCase):

    @patch("Parser.Drivers")
    def test_add_driver(self, mock_drivers):
        m = mock_open(read_data="Driver Adam")
        with patch('builtins.open', m):
            parse_input("/a/b/c")
            mock_drivers().add_driver.assert_called_with("Adam")


if __name__ == '__main__':
    unittest.main()