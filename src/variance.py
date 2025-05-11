
def variance(data_array):
    """ """
    if len(data_array) == 0:
        return 0

    mean = sum(data_array) / len(data_array)

    print("mean", mean)
    p2s = map(lambda x: (x - mean) ** 2, data_array)
    variance = sum(p2s) / len(data_array)
    return variance
