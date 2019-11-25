import numpy as np

'''
Returns the indices of the n max values in an array
'''
def n_max_indices(array, max_n):
    if type(array) is list:
        array = np.array(array)
    indices = array.ravel().argsort()[-max_n:]
    return indices[::-1]
