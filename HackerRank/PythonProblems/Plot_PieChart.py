import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0.1, 0, 0]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, startangle = 90, explode = myexplode, shadow = True, colors = mycolors)
plt.legend(title = "Four Fruits")

# The explode parameter, if specified, and not None, must be an array with one value for each wedge.
'''
By default the plotting of the first wedge starts from the x-axis and move counterclockwise
The size of each wedge is determined by comparing the value with all the other values, by using this formula:
The value divided by the sum of all values: x/sum(x)
'''








plt.show() 