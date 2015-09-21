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

import tf_libs as tf

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

def built_in_examples():

    print('*** built_in_examples ***\n')

    x=[["a","b","c"], ["d","e","f"], ["g","h","i","j"]]
    print('x=[["a","b","c"], ["d","e","f"], ["g","h","i","j"]]')

    print("\n[j for i in x for j in i]  - list comprehension example")
    print([j for i in x for j in i])

    print("with open(\"test.txt\") as f:  -  Deals with automatically closing file after use")
    with open("test.txt") as f:
        data = f.read()
        print(data)


def std_libs_examples():

    x=[["a","b","c"], ["d","e","f"], ["g","h","i","j"]]
    print('x=[["a","b","c"], ["d","e","f"], ["g","h","i","j"]]')

    ## Nested lists
    import itertools
    print("\nlist(itertools.chain(*x)) - removes nested lists")
    print(list(itertools.chain(*x)))

    ## Named Tuples
    import collections
    Person = collections.namedtuple('Person', 'name age gender')
    print('\nType of Person:', type(Person))
    bob = Person(name='Bob', age=30, gender='male')
    print('Representation:', bob)
    jane = Person(name='Jane', age=29, gender='female')
    print('Field by name:', jane.name)
    print('Fields by index:')
    for p in [ bob, jane ]:
        print('%s is a %d year old %s' % p)
    ## Note: Cannot change values eg: jane.name = 'Janey'

    ## Ordered dictionary
    print('\nRegular dictionary:')
    d = {}
    d['a'] = 'A'
    d['b'] = 'B'
    d['c'] = 'C'
    d['d'] = 'D'
    d['e'] = 'E'

    for k, v in d.items():
        print(k, v)

    print('\nOrderedDict:')
    d = collections.OrderedDict()
    d['a'] = 'A'
    d['b'] = 'B'
    d['c'] = 'C'
    d['d'] = 'D'
    d['e'] = 'E'

    for k, v in d.items():
        print(k, v)

    ## Default dictionary - default value for unassigned keys - no KeyError
    def default_factory():
        return None  #'default value'

    d = collections.defaultdict(default_factory, foo='bar')
    print('\nd:', d)
    print('foo =>', d['foo'])
    print('bar =>', d['bar'])

    ## Decimal
    import decimal # Alows exact decimal numbers - not floating point, so can have exact 0.1, 0.2, 6.1 etx
    fmt = '{0:<20} {1:<20}'
    print(fmt.format('\nInput', 'Output'))
    print(fmt.format('-' * 20, '-' * 20))
    # Integer
    print(fmt.format(5, decimal.Decimal(5)))
    # String
    print(fmt.format('3.14', decimal.Decimal('3.14')))
    # Float
    print(fmt.format(repr(0.1), decimal.Decimal(str(0.1))))

    ## sys - command line arguments
    # import sys
    # arg = sys.argv[1]
    ## to be used like:
    ## $ python script.py arg_string

    ## CSV
    ##Reading
    import csv
    f = open('test.txt', 'rt')
    try:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print(row, end=' ')
    finally:
        f.close()
    ## Writing
    f = open('test.csv', 'wt')
    try:
        writer = csv.writer(f)
        writer.writerow( ('Title 1', 'Title 2') )
        for i in range(10):
            writer.writerow( (i+1, chr(ord('a') + i), '08/%02d/15' % (i+1)) )
    finally:
        f.close()

    # print(open('test.csv', 'rt').read())

    ## Time - sleep
    import time

    for i in range(11):
        phase = 'Phase %d' % i
        print(phase)
        time.sleep(0.2)
    print('Done with loop')

    time.sleep(1)


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

    bins = [0,3,7,22,24,100,101]
    print("\nnp.digitize(arr, bins) - returns index of bin to which each data element belongs (index is for upper bound of bin - bins[i-1] <= x < bins[i])")
    print(np.digitize(arr, bins))# - binning data

    print("\nnp.clip(arr, 1.256, 8.2) - move points outside range to boundaries:")
    print(np.clip(arr, 1.256, 8.2))

    print("np.pad(arr, [6,10], mode='reflect') - pad ends of array with constants, max/min or reflections etc")
    print(np.pad(arr, [6,10], mode='reflect'))

    print("\nnp.flat(arr)- Return a copy of the array collapsed into one dimension.")
    print(arr.flatten()) #- removes nested lists in numpy array

    print("np.column_stack((arr,arr*2)) - turn 1D arrays into columns - ideal for file writing with numpy.savetxt")
    print(np.column_stack((arr,arr*2)))

    data = np.column_stack((arr,arr*2))
    print("np.savetxt('test.txt', data, fmt=('%10.5g','%10.5g'), delimiter=' ', header='col1\tcol2') save arrays as text files")
    print(np.savetxt('test.txt', data, fmt=('%10.5g','%10.5g'), delimiter=' ', header='col1\tcol2'))

    print("col1, col2 = np.loadtxt('test.txt', usecols=(0,1), unpack=True) - load text file produced with numpy.savetxt")
    print(np.loadtxt('test.txt', usecols=(0,1), unpack=True))

    print("\nnp.isnan([1,np.nan,48646.418654])")
    print(np.isnan([1,np.nan,48646.418654]))

    print("\nnp.fromstring('1 2 3 4', dtype=int, sep=' ')")
    print(np.fromstring('1 2 3 4', dtype=int, sep=' '))



    ## Useful ndarray methods:
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

def sp_examples():

    rnd_arr = np.random.rand(20)
    print("np.random.rand(20)")
    print(rnd_arr)

    # sp.signal.find_peaks_cwt - peak finding, returns peak indices, 2nd arguement is array of values
    # covering expected peak width range
    print("sp.signal.find_peaks_cwt(rnd_arr, np.linspace(0.2,0.4, 10))")
    peakind = sp.signal.find_peaks_cwt(rnd_arr, np.linspace(0.2,0.4, 10))
    print(peakind)

    fig = plt.figure()
    plt.plot(np.arange(20), rnd_arr, 'b--o', color = 'blue' )
    plt.plot(peakind, rnd_arr[peakind], 'o', color="red" )
    plt.title='sp.signal.find_peaks_cwt'
    plt.show()

def mpl_examples():
    ## Using color maps - example from http://stackoverflow.com/questions/8931268/using-colormaps-to-set-color-of-line-in-matplotlib
    # define some random data that emulates your intended code:
    import matplotlib.pyplot as plt
    import matplotlib
    import numpy as np
    NCURVES = 10
    np.random.seed(101)
    curves = [np.random.random(20) for i in range(NCURVES)]
    values = range(NCURVES)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    jet = cm = plt.get_cmap('jet')
    cNorm  = matplotlib.colors.Normalize(vmin=0, vmax=values[-1])
    scalarMap = matplotlib.cm.ScalarMappable(norm=cNorm, cmap=jet)
    print(scalarMap.get_clim())

    lines = []
    for idx in range(len(curves)):
        line = curves[idx]
        colorVal = scalarMap.to_rgba(values[idx])
        colorText = (
            'color: (%4.2f,%4.2f,%4.2f)'%(colorVal[0],colorVal[1],colorVal[2])
            )
        retLine, = ax.plot(line,
                           color=colorVal,
                           label=colorText)
        lines.append(retLine)
    ## Legend
    handles,labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc='upper right')
    ax.grid()
    plt.show()

if __name__ == "__main__":
    built_in_examples()
    # std_libs_examples()
    # np_examples()
    # sp_examples()
    # mpl_examples()
    pass