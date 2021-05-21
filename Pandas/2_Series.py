import pandas as pd

a = [1, 7, 2]

#Create a simple Pandas Series from a list
myvar = pd.Series(a)
print(myvar)

#Labels => This label can be used to access a specified value.
print(myvar[0])

#Create Labels
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

#Key/Value Objects as Series
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)
print(myvar)

#To select only some of the items in the dictionary
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

#DataFrames => usually multi-dimensional tables
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)
print(myvar)








