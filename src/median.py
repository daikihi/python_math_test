import math
import statistics

from src.mean import Mean

class Median:
    def median(self,data_array):
        """
        return the median of a list of numbers
        if the list is empty, return 0
        if the list has an even number of elements, return the average of the two middle elements
        if the list has an odd number of elements, return the middle element
        """
        if len(data_array) == 0:
            return [0]
        elif len(data_array) == 1:
            return data_array[0]
        else:
            data_array.sort()
            indexes  = self._get_median_index(data_array)
            response_values = []
            for i in indexes: 
                response_values.append(data_array[i - 1]) # array index starts from 0
            return Mean().mean(response_values)

    def lib_used_median(self,data_array):
        return statistics.median(data_array)

    # should be private and used only for median function
    def _get_median_index(self, data_array):
        """ """
        if len(data_array) % 2 == 1:
            target_indexes = [int((len(data_array) + 1 ) / 2)]
        else:
            target_indexes = [int(math.ceil(len(data_array) / 2)), int(math.ceil((len(data_array) + 1)  / 2))]
        return target_indexes 
    
