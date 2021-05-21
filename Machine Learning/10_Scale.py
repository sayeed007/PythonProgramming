'''
The standardization method uses this formula:
z = (x - u) / s
Where z is the new value, 
x is the original value, 
u is the mean and 
s is the standard deviation
'''
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

df = pandas.read_csv("cars2.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)

#Predict CO2 Values
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print('Predict CO2 Values :', predictedCO2)



















