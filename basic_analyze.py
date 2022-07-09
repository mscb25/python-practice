# Counter can be used to determine how many times an item appears in a list

from collections import Counter
from collections import *

ages = [22, 23, 45, 72, 13, 13, 22, 25, 29, 8]

print(Counter(ages))


#enumerate is helpful function to add a counter to a loop

names = ['Maddie', 'Dominic', 'Tommy', 'Erin', 'Mack']

for i, name in enumerate(names):
    print("Index: {}".format(i))
    print("Value: {}".format(name))


#creates a new list of all the names that have more than 5 characters
long_name = [x for x in names if len(x) > 5]

print(long_name)

#organizes the list numerically

'''
sort_list = ages.sort()
print(sort_list)
'''

#turning lists into tuples and back

first = ['Maddie', 'Erin', 'Teal']
second = ['Swimming', 'Lacrosse', 'Basketball']

tups = list(zip(first, second))
print(tups)

name, sport = zip(*tups)
print(name)
print(sport)


# numpy has a shuffle function, which is pretty cool

import numpy as np

arr = [0, 1, 2, 3, 4, 5]
np.random.shuffle(arr)
print(arr)


# cumulative distribution.. aka how likely you are to sample a value less than or equal to x

from scipy import stats

prob = stats.norm.cdf(x=0, loc=0, scale=10) # prob of sampling 0 when mean is 0 and std is 10
print(prob)


# calculating the basic elements of array

def get_the_basics(array):
    maximum = np.max(array)
    stand = np.std(array)
    summation = np.sum(array)
    dot = np.dot(array, array)
    return maximum, stand, summation, dot


# function to calculate the correlation between two graphs (aka r value)

def find_correlation(array1, array2):
    return stats.pearsonr(array1, array2)
