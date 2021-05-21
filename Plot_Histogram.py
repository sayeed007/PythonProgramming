import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)
#Printing X value
print(x)

#Showing X's value in histogram
plt.hist(x)
plt.show() 