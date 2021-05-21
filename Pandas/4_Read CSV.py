import pandas as pd

#Load the CSV into a DataFrame
df = pd.read_csv('data.csv')

#By default, when you print a DataFrame, you will only get the first 5 rows, and the last 5 rows
print(df) 

##use to_string() to print the entire DataFrame.
print(df.to_string())  








