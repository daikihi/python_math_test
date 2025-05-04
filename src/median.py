import math


def median(data_array):
    """
    return the median of a list of numbers
    if the list is empty, return 0
    if the list has an even number of elements, return the average of the two middle elements
    if the list has an odd number of elements, return the middle element
    """
    if len(data_array) == 0:
        return [0]
    elif len(data_array) == 1:
        return data_array
    else:
        data_array.sort()
        indexes  = _get_median_index(data_array)
        response_values = []
        for i in indexes: 
            print("i: ", i)
            print("len(data_array): ", len(data_array))
            print("data_array[i]: ", data_array[i])
            response_values.append(data_array[i - 1]) # array index starts from 0
        return response_values


def _get_median_index(data_array):
    """ """
    if len(data_array) % 2 == 1:
        target_indexes = [int((len(data_array) + 1 ) / 2)]
    else:
        target_indexes = [int(math.ceil(len(data_array) / 2)), int(math.ceil((len(data_array) + 1)  / 2))]
    return target_indexes 