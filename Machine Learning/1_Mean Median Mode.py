import numpy
from scipy import stats

speed = [99,86,87,88,86,103,87,94,78,77,85,86]

#Mean (sum/total count)
print('Mean of the array value: ')
x = numpy.mean(speed)
print(x)

#Median (middle value after sorting)
print('Median of the array value: ')
x = numpy.median(speed)
print(x)

#Mode   (maximum occurance value)
print('Mode of the array value: ')
x = stats.mode(speed)
print(x)













