import unittest
from src.stattistic.variance import variance

class TestVariance(unittest.TestCase):
    def test_variance(self):
        assert variance([1, 2, 3, 4, 5]) == 2.0
        assert variance([1, 2, 3]) == 2/3
        assert variance([1]) == 0.0
        assert variance([]) == 0.0
        assert variance([1, 2, 3, 4]) == 1.25
        assert variance([10, 20, 30]) == 200.0/3
        assert variance([-1, -2, -3]) == 2/3
        assert variance([1.5, 2.5, 3.5]) == 2/3
