import numpy as np

def add_arrays(array1, array2):
    if array1.shape != array2.shape:
        raise ValueError("Arrays must have the same shape for addition.")
    return array1 + array2

def calculate_mean(array):
    return np.mean(array)


#Test Cases
import pytest

def test_add_arrays():
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])
    result = add_arrays(array1, array2)
    expected_result = np.array([5, 7, 9])
    assert np.array_equal(result, expected_result)

