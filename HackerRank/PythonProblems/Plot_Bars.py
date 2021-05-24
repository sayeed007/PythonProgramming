import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 2, 1)
plt.bar(x,y, color = "green", width = 0.2,)


#Horizontal Bars
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 2,2 )
plt.barh(x, y, color = "hotpink", height = 0.3)
#For horizontal bars, use height instead of width











plt.show()
