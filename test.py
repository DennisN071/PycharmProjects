import numpy as npy
from scipy import stats
speed = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

mean = npy.mean(speed)
median = npy.median(speed)
mode = stats.mode(speed)
standard_deviation = npy.std(speed)
variance = npy.var(speed)

print('The mean is', mean)
print('The median is', median)
print('The mode is', mode)
print('The standard_deviation is', standard_deviation)
print('The variance is ', variance)