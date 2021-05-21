import pandas as pd

df = pd.read_csv('data.csv')

#The corr() method ignores "not numeric" columns.
print(df.corr())
























