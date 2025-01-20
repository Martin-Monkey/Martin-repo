# main.py

import unittest
from cislo import Number  # Import the Number class


class TestNumber(unittest.TestCase):

    def test_set_and_get_value(self):
        num = Number(10)
        self.assertEqual(num.get_value(), 10)  # Verify the value is correctly set to 10
        num.set_value(20)
        self.assertEqual(num.get_value(), 20)  # Verify the value is updated to 20

    def test_to_octal(self):
        num = Number(10)
        self.assertEqual(num.to_octal(), '12')  # 10 in octal is 12

        num = Number(64)
        self.assertEqual(num.to_octal(), '100')  # 64 in octal is 100

    def test_to_hexadecimal(self):
        num = Number(10)
        self.assertEqual(num.to_hexadecimal(), 'a')  # 10 in hexadecimal is 'a'

        num = Number(255)
        self.assertEqual(num.to_hexadecimal(), 'ff')  # 255 in hexadecimal is 'ff'

    def test_to_binary(self):
        num = Number(10)
        self.assertEqual(num.to_binary(), '1010')  # 10 in binary is 1010

        num = Number(64)
        self.assertEqual(num.to_binary(), '1000000')  # 64 in binary is 1000000


if __name__ == "__main__":
    unittest.main()  # Runs all tests if this file is executed directly
