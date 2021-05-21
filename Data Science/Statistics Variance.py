import pandas as pd
import numpy as np

'''
    Calculating Varience:::
    Step 1: to Calculate the Variance: Find the Mean
    Step 2: For Each Value - Find the Difference From the Mea
    Step 3: For Each Difference - Find the Square Value
    The Variance is the Average Number of These Squared Values
'''
#USING PYTHON FOR THE ABOVE TASK​
health_data = pd.read_csv("data.csv", header=0, sep=",")

var = np.var(health_data)

print("Variance of the data:", var)


 