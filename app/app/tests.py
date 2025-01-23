"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add(self):
        self.assertEqual(calc.add(5, 6), 11)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 15), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
