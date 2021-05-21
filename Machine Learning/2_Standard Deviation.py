'''
Standard deviation is a number that describes how spread out the values are.
A low standard deviation means that most of the numbers are close to the mean (average) value.
A high standard deviation means that the values are spread out over a wider range.
'''
import numpy

speed = [86,87,88,86,87,85,86]

#Standard Deviation => Standard Deviation is often represented by the symbol Sigma: σ
#First find mean then the max difference between lowest or height value of the array/dataset
print('Standard Deviation of the array is: ')
x = numpy.std(speed)
print(x)


#Variance => Variance is often represented by the symbol Sigma Square: σ2
#if you multiply the standard deviation by itself, you get the variance!
print('Variance of the array is: ')
x = numpy.var(speed)
print(x)











