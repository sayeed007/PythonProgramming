#Find if the given values v1 and v2 are from same distribution:
import numpy as np
from scipy.stats import ttest_ind


print("T-Test")
#T-tests are used to determine if there is significant deference between means of two variables
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)
#ttest_ind() takes two samples of same size 
# and produces a tuple of t-statistic and p-value.
#P-value => tells how close to extreme the data actually is.
print(res)
print(res.pvalue)

print("\nKS-Test")
#KS test is used to check if given values follow a distribution.
from scipy.stats import kstest

v = np.random.normal(size=100)

res = kstest(v, 'norm')
print(res)


print("\nStatistical Description of Data")
#In order to see a summary of values in an array, we can use the describe() function.
from scipy.stats import describe

v = np.random.normal(size=100)
res = describe(v)

print(res)

print("\nNormality Tests (Skewness and Kurtosis)")
'''
    Skewness: A measure of symmetry in data.
    For normal distributions = 0, negative = skewed left, positive = skewrd right

    Kurtosis: A measure of whether the data is heavy or lightly tailed to a normal distribution.
    Positive = heavy tailed, Negative = lightly tailed.
'''
from scipy.stats import skew, kurtosis

v = np.random.normal(size=100)

print("Skewness = ", skew(v))
print("Kurtosis = ", kurtosis(v))

from scipy.stats import normaltest
print("\nNormal Test = ", normaltest(v))
#The normaltest() function returns p value for the null hypothesis



