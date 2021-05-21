import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)

#Locate Row
#refer to the row index:    This example returns a Pandas Series.
print("Values of first index \n",df.loc[0])

#Return row 0 and 1:        use a list of indexes:
print(df.loc[[0, 1]])
#When using [], the result is a Pandas DataFrame

#Named Indexes
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print("datas with specific indexes: \n", df) 

#Locate Named Indexes
print(df.loc["day2"])

#Load Files Into a DataFrame
import pandas as pd

df = pd.read_csv('data.csv')
print(df) 









