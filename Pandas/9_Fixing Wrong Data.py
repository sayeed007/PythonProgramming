import pandas as pd

df = pd.read_csv('dirtydata.csv')

df.loc[7,'Duration'] = 45
print(df.to_string())


#Loop through all values in the "Duration" column.
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

print(df.to_string())

###Removing Rows
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

#remember to include the 'inplace = True' argument to make the changes in the original DataFrame object instead of returning a copy

print(df.to_string())














