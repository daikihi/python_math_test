import unittest
from src.caliculus.simple_integral import SimpleIntegral

class TestSimpleIntegral(unittest.TestCase):
    def test_simple_integral(self):
        """ y = 1*x + 0"""
        self.assertEqual(SimpleIntegral().simple_integral(1, 0, 0, 10, 1.0), 45.0)
        """ y = 2*x + 1"""
        self.assertEqual(SimpleIntegral().simple_integral(2, 1, 0, 10, 1), 100.0)
        """ y = -1*x + 5"""
        self.assertEqual(SimpleIntegral().simple_integral(-1, 5, 0, 10, 1), 5.0)
        """ y = -2*x + 3"""
        self.assertEqual(SimpleIntegral().simple_integral(-2, 3, 0, 10, 1), -60.0)
        """ y = 3*x + -2"""
        self.assertEqual(SimpleIntegral().simple_integral(3, -2, 0, 10, 1), 115.0)

if __name__ == "__main__":
    unittest.main()