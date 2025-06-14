import unittest
from src.stattistic.mean import Mean  # 修正: インポートパスを変更

class TestMean(unittest.TestCase):
    """unit testing for mean.py"""
    def test_mean(self):
        """ empty array input returns 0 """
        empty_request = []
        empty_result = Mean().mean(empty_request)
        # statistics.mean() does not support empty array for input
        # empty_result_lib = Mean().lib_used_mean(empty_request)
        self.assertEqual(empty_result, 0)
        # self.assertEqual(empty_result_lib, empty_result)

        """ single element of array returns the element value"""
        single_request = [5]
        single_result = Mean().mean(single_request)
        single_result_lib = Mean().lib_used_mean(single_request)
        self.assertEqual(single_result, 5)
        self.assertEqual(single_result_lib, single_result)

        """ multiple elements of array returns the mean value"""
        multiple_request = [1, 2, 3, 4, 5]
        multiple_result = Mean().mean(multiple_request)
        multiple_result_lib = Mean().lib_used_mean(multiple_request)
        self.assertEqual(multiple_result, 3)
        self.assertEqual(multiple_result_lib, multiple_result)

        """ negative elements of array returns the mean value"""
        negative_request = [-1, -2, -3, -4, -5]
        negative_result = Mean().mean(negative_request)
        negative_result_lib = Mean().lib_used_mean(negative_request)
        self.assertEqual(negative_result, -3)
        self.assertEqual(negative_result_lib, negative_result)

        """ mixed elements of array returns the mean value"""
        mixed_request = [-1, 2, -3, 4, -5]
        mixed_result = Mean().mean(mixed_request)
        mixed_result_lib = Mean().lib_used_mean(mixed_request)
        self.assertEqual(mixed_result, -0.6)
        self.assertEqual(mixed_result_lib, mixed_result)

        """ large numbers of array returns the mean value"""
        large_request = [1000000, 2000000, 3000000, 4000000, 5000000]
        large_result = Mean().mean(large_request)
        large_result_lib = Mean().lib_used_mean(large_request)
        self.assertEqual(large_result, 3000000)
        self.assertEqual(large_result_lib, large_result)

        """ large negative numbers of array returns the mean value"""
        large_negative_request = [-1000000, -2000000, -3000000, -4000000, -5000000]
        large_negative_result = Mean().mean(large_negative_request)
        large_negative_result_lib = Mean().lib_used_mean(large_negative_request)
        self.assertEqual(large_negative_result, -3000000)
        self.assertEqual(large_negative_result_lib, large_negative_result)
        
        """ large mixed numbers of array returns the mean value"""
        large_mixed_request = [-1000000, 2000000, -3000000, 4000000, -5000000]
        large_mixed_result = Mean().mean(large_mixed_request)
        large_mixed_result_lib = Mean().lib_used_mean(large_mixed_request)
        self.assertEqual(large_mixed_result, -600000)
        self.assertEqual(large_mixed_result_lib, large_mixed_result)

        """ decimal numbers of array returns the mean value"""
        decimal_numbers_request = [1.5, 2.5, 3.5, 4.5, 5.5]
        decimal_numbers_result = Mean().mean(decimal_numbers_request)
        decimal_numbers_result_lib = Mean().lib_used_mean(decimal_numbers_request)
        self.assertEqual(decimal_numbers_result, 3.5)
        self.assertEqual(decimal_numbers_result_lib, decimal_numbers_result)

        """ decimal negative numbers of array returns the mean value"""
        decimal_negative_numbers_request = [-1.5, -2.5, -3.5, -4.5, -5.5]
        decimal_negative_numbers_result = Mean().mean(decimal_negative_numbers_request)
        decimal_negative_numbers_result_lib = Mean().lib_used_mean(decimal_negative_numbers_request)
        self.assertEqual(decimal_negative_numbers_result, -3.5)
        self.assertEqual(decimal_negative_numbers_result_lib, decimal_negative_numbers_result)

        """ decimal mixed numbers of array returns the mean value"""
        decimal_mixed_numbers_request = [-1.5, 2.5, -3.5, 4.5, -5.5]
        decimal_mixed_numbers_result = Mean().mean(decimal_mixed_numbers_request)
        decimal_mixed_numbers_result_lib = Mean().lib_used_mean(decimal_mixed_numbers_request)
        self.assertEqual(decimal_mixed_numbers_result, -0.7)
        self.assertEqual(decimal_mixed_numbers_result_lib, decimal_mixed_numbers_result)

        """ decimal numbers of array returns the mean value"""
        decimal_numbers_request = [1.5, 2.5, 3.5, 4.5, 5.5]
        decimal_numbers_result = Mean().mean(decimal_numbers_request)
        decimal_numbers_result_lib = Mean().lib_used_mean(decimal_numbers_request)
        self.assertEqual(decimal_numbers_result, 3.5)
        self.assertEqual(decimal_numbers_result_lib, decimal_numbers_result)
        
        """ decimal negative numbers of array returns the mean value"""
        deciaml_negative_numbers_request = [-1.5, -2.5, -3.5, -4.5, -5.5]
        decimal_negative_numbers_result = Mean().mean(deciaml_negative_numbers_request)
        decimal_negative_numbers_result_lib = Mean().lib_used_mean(deciaml_negative_numbers_request)
        self.assertEqual(decimal_negative_numbers_result, -3.5)
        self.assertEqual(decimal_negative_numbers_result_lib, decimal_negative_numbers_result)
        
if __name__ == "__main__":
    unittest.main()