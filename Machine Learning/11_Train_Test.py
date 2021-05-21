import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)

#Start Creating With a Data Set
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.subplot(2, 2, 1)
plt.title('Total Dataset')
plt.scatter(x, y)

#Split Into Train/Test
train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

#Display the Training Set
plt.subplot(2, 2, 2)
plt.scatter(train_x, train_y, color = 'hotpink')
plt.scatter(test_x, test_y, color = 'lightgreen')
plt.title("Train & Test Datas")

#Fit the Data Set
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.subplot(2, 2, 3)
plt.scatter(train_x, train_y, color = 'yellow')
plt.plot(myline, mymodel(myline), color = 'black')
plt.title("Fitting the Training Data Set")

#R-squared for train data
r2 = r2_score(train_y, mymodel(train_x))

print('the relationship between the x axis and the y axis => \nR-squared value for train data: :', r2)

#R-squared for Testing Set
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(test_y, mymodel(test_x))

print('R-squared value for test data: ', r2)

#Predict Values
print('Predicted Values for 5min position: ', mymodel(5))









plt.show()














