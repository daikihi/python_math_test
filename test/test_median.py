import unittest
from src.median import median 

class TestMedian(unittest.TestCase):
    def test_median(self):
        """ empty array returns 0"""
        self.assertEqual(median([]), [0])
        """ single element of array returns the element value"""
        single_result = median([5])
        self.assertEqual(single_result, 5)
        """ multiple elements of array returns the median value"""
        multiple_result = median([1, 2, 3, 4, 5])
        self.assertEqual(multiple_result, 3)
        """ even number of elements of array returns the average of the two middle elements"""
        even_result = median([1, 2, 3, 4])
        self.assertEqual(even_result, 2.5)
        """ negative elements of array returns the median value"""
        negative_result = median([-1, -2, -3, -4, -5])
        self.assertEqual(negative_result, -3)
        """ mixed elements of array returns the median value"""
        mixed_result = median([-1, 2, -3, 4, -5])
        self.assertEqual(mixed_result, -1)

if __name__ == "__main__":
    unittest.main()