import numpy as np

class SimpleIntegral:
    def simple_integral(self, a, b, x_from, x_to, intervals):
        """
        function: y = a * x + b
        """
        if x_from >= x_to:
            raise ValueError("x_from must be less than x_to")
        
        if intervals <= 0:
            raise ValueError("Number of intervals must be a positive integer")

        result = 0.0
        for i in np.arange(x_from , x_to, intervals):
            x = i
            y = (a * x) + b
            size = y * intervals
            result += size
        return result
