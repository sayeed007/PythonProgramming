import numpy

print('Creating 500 random float data:')
x = numpy.random.uniform(0.0, 5.0, 500)

print(x)

#Histogram
import matplotlib.pyplot as plt
print('ploting the dataset')

plt.hist(x, 5)  # 5 => total number of bars 
plt.show()


x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()






