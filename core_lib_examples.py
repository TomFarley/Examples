#!/usr/bin/env python

""" core_lib_examples.py: Example usages of core python functions.

Keyword arguments:
    newarg -- type, description (default 0.0)
    newarg -- type, description (default 0.0)

Detailed description:

Notes:
    @bug:

Reminders:
    @todo:

Info:
    @since: 00-00-15
"""

import numpy as np                  # Maths library
import scipy as sp                  # Data analysis library
import matplotlib.pyplot as plt     # Plotting library

from scipy.optimize import curve_fit                # Curve fitting
from scipy.signal import find_peaks_cwt, argrelmax  # Peak finding
from scipy.interpolate import interp1d              # Interpolation

import os           # System directory/file operations
import shutil       # High-level file operations
import re           # Regular expressions

from pprint import pprint   # Pretty printing

__author__ = 'Tom Farley'
__copyright__ = "Copyright 2015, TF Library Project"
__credits__ = []
__email__ = "farleytpm@gmail.com"
__status__ = "Development"
__version__ = "1.0.1"

arr = np.linspace(0,25,51)
arr2 = np.linspace(16,36,21)
ends = [11,23.42]
strings = ['Tom', 'Farley', 'Ellie', 'Corney']
string = 'Farley'

def np_examples():
    """ Examples of useful numpy functions """
    print('\n*** np_examples ***')
    print('arr = ',)
    print(arr, '\n')
    print('arr2 = ',)
    print(arr2, '\n')

    ## np.extract - filter array based on condition (~like where in IDL):
    ## sub_arr = np.extract(condition, orig_arr)
    ## np.extract((5 <= a) * (a <= 15), a), arange(20)) will return array containing 5-15
    print("np.extract((arr >= 11) * (arr <= 23.42), arr)")
    print(np.extract((arr >= 11) * (arr <= 23.42), arr))

    print("\nnp.intersect1d(arr,arr2) - return intersection of a and b")
    print(np.intersect1d(arr,arr2))

    print("\nnp.union1d(arr,arr2) - return union of a and b")
    print(np.union1d(arr,arr2))

    print("\nnp.setdiff1d(arr,arr2) - elements unique to A only")
    print(np.setdiff1d(arr,arr2))

    print("\nnp.setxor1d(arr,arr2) - in A or B but not both")
    print(np.setxor1d(arr,arr2))

    # np.in1d - Returns a boolean array the same length as ar1 that is True where an element of ar1 is in ar2 and False otherwise.
    print("\nnp.in1d(arr,arr2) - Test whether each element of a 1-D array is also present in a second array.")
    print(np.in1d(arr,arr2))

    print("\nnp.fix(arr) - round towards zero")
    print(np.fix(arr))

    # numpy.digitize - binning data
#
#     np.clip - move points outside range to boundaries:
# >>> a = np.arange(10)
# >>> np.clip(a, 1, 8)
# array([1, 1, 2, 3, 4, 5, 6, 7, 8, 8])
#
# ndarray.flat - removes nested lists in numpy array
#
# np.lib.pad - pad ends of array with constants, max/min or reflections etc


    print("np.column_stack((arr,arr*2)) - turn 1D arrays into columns - ideal for file writing with numpy.savetxt")
    print(np.column_stack((arr,arr*2)))

    data = np.column_stack((arr,arr*2))
    print("np.savetxt('test.txt', data, fmt=('%10.5g','%10.5g'), delimiter=' ', header='col1\tcol2') save arrays as text files")
    print(np.savetxt('test.txt', data, fmt=('%10.5g','%10.5g'), delimiter=' ', header='col1\tcol2'))

    print("col1, col2 = np.loadtxt('test.txt', usecols=(0,1), unpack=True) - load text file produced with numpy.savetxt")
    print(np.loadtxt('test.txt', usecols=(0,1), unpack=True))


# ndarray.take(indices[, axis, out, mode])	Return an array formed from the elements of a at the given indices.
# ndarray.put(indices, values[, mode])	Set a.flat[n] = values[n] for all n in indices.
# ndarray.sort([axis, kind, order])	Sort an array, in-place.
# ndarray.argsort([axis, kind, order])	Returns the indices that would sort this array.
# ndarray.nonzero()	Return the indices of the elements that are non-zero.
# ndarray.argmax([axis, out])	Return indices of the maximum values along the given axis.
# ndarray.min([axis, out])	Return the minimum along a given axis.
# ndarray.ptp([axis, out])	Peak to peak (maximum - minimum) value along a given axis.
# ndarray.clip(a_min, a_max[, out])	Return an array whose values are limited to [a_min, a_max].
# ndarray.round([decimals, out])	Return a with each element rounded to the given number of decimals.
# ndarray.sum([axis, dtype, out])	Return the sum of the array elements over the given axis.
# ndarray.cumsum([axis, dtype, out])	Return the cumulative sum of the elements along the given axis.
# ndarray.mean([axis, dtype, out])	Returns the average of the array elements along given axis.
# ndarray.var([axis, dtype, out, ddof])	Returns the variance of the array elements, along given axis.
# ndarray.std([axis, dtype, out, ddof])	Returns the standard deviation of the array elements along given axis.
# ndarray.all([axis, out])	Returns True if all elements evaluate to True.
# ndarray.any([axis, out])	Returns True if any of the elements of a evaluate to True.




if __name__ == "__main__":
    np_examples()
    pass