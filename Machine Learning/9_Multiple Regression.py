import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]    #list of the independent values and call this variable X
y = df['CO2']       #the dependent values in a variable called y.

regr = linear_model.LinearRegression()  #create a linear regression object
regr.fit(X, y)
'''
This object has a method called fit() that takes the independent 
and dependent values as parameters and fills the regression object with data 
that describes the relationship
'''

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)

#Coefficient
print('the coefficient values of the regression object: ', regr.coef_)













