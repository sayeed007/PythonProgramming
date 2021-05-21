import pandas as pd

df = pd.read_csv('dirtydata.csv')

###Discovering Duplicates
print(df.duplicated())

###Removing Duplicates
df.drop_duplicates(inplace = True)
print(df.to_string())


















#Discovering Duplicates