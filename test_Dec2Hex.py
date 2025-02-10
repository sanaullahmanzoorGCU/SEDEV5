import unittest
from Dec2Hex import decimal_to_hex

class TestDec2Hex(unittest.TestCase):
    def test_decimal_to_hex(self):
        # Test case 1: Decimal 10 should return 'A'
        self.assertEqual(decimal_to_hex(10), 'A')

        # Test case 2: Decimal 255 should return 'FF'
        self.assertEqual(decimal_to_hex(255), 'FF')

        # Test case 3: Decimal 16 should return '10'
        self.assertEqual(decimal_to_hex(16), '10')

        # Test case 4: Decimal 0 should return an empty string
        self.assertEqual(decimal_to_hex(0), '')

if __name__ == '__main__':
    unittest.main()
