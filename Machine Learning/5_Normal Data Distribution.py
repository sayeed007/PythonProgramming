import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000) #normal(mean, standerd deviation, total count)

plt.hist(x, 100)
plt.show()