import statistics

class Mean:
    def mean(self, data_array):
        """ """
        if len(data_array) == 0:
            return 0
        return sum(data_array) / len(data_array)
    
    def lib_used_mean(self, data_array):
        """ """
        return statistics.mean(data_array)