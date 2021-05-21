import pandas as pd

df = pd.read_csv('data.csv')

#Viewing the Data
print(df.head(10))
# if the number of rows is not specified, the head() method will return the top 5 rows

#tail() method for viewing the last rows of the DataFrame
print(df.tail(10)) 

#Info About the Data
print(df.info()) 

#The info() method also tells us how many Non-Null values there are present in each column, 


















