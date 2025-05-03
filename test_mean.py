import unittest
from mean import mean


class TestMean(unittest.TestCase):
    """unit testing for mean.py"""
    def test_mean(self):
        print("test_mean.....")
        """ empty array input returns 0 """
        empty_result = mean([])
        self.assertEqual(empty_result, 0)
        """ single element of array returns the element value"""
        single_result = mean([5])
        self.assertEqual(single_result, 5)
        """ multiple elements of array returns the mean value"""
        multiple_result = mean([1, 2, 3, 4, 5])
        self.assertEqual(multiple_result, 3)
        """ negative elements of array returns the mean value"""
        negative_result = mean([-1, -2, -3, -4, -5])
        self.assertEqual(negative_result, -3)
        """ mixed elements of array returns the mean value"""
        mixed_result = mean([-1, 2, -3, 4, -5])
        self.assertEqual(mixed_result, -0.6)
        """ large numbers of array returns the mean value"""
        large_result = mean([1000000, 2000000, 3000000, 4000000, 5000000])
        self.assertEqual(large_result, 3000000)
        """ large negative numbers of array returns the mean value"""
        large_negative_result = mean([-1000000, -2000000, -3000000, -4000000, -5000000])
        self.assertEqual(large_negative_result, -3000000)
        """ large mixed numbers of array returns the mean value"""
        large_mixed_result = mean([-1000000, 2000000, -3000000, 4000000, -5000000])
        self.assertEqual(large_mixed_result, -600000)
        """ large numbers of array returns the mean value"""
        large_numbers_result = mean([1.5, 2.5, 3.5, 4.5, 5.5])
        self.assertEqual(large_numbers_result, 3.5)
        """ large negative numbers of array returns the mean value"""
        large_negative_numbers_result = mean([-1.5, -2.5, -3.5, -4.5, -5.5])
        self.assertEqual(large_negative_numbers_result, -3.5)
        """ large mixed numbers of array returns the mean value"""
        large_mixed_numbers_result = mean([-1.5, 2.5, -3.5, 4.5, -5.5])
        self.assertEqual(large_mixed_numbers_result, -0.7)
        """ large numbers of array returns the mean value"""
        large_numbers_result = mean([1.5, 2.5, 3.5, 4.5, 5.5])
        self.assertEqual(large_numbers_result, 3.5)
        """ large negative numbers of array returns the mean value"""
        large_negative_numbers_result = mean([-1.5, -2.5, -3.5, -4.5, -5.5])
        self.assertEqual(large_negative_numbers_result, -3.5)
if __name__ == "__main__":
    unittest.main()