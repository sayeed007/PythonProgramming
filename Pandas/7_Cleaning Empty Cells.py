import pandas as pd

df = pd.read_csv('dirtydata.csv')
print(df.to_string())

#By default, the dropna() method returns a new DataFrame, and will not change the original.
new_df = df.dropna()
print(new_df.to_string())

#If you want to change the original DataFrame, use the inplace = True argument
#df.dropna(inplace = True)
#print(df.to_string())

#Replace Empty Values
df.fillna(130, inplace = True)

#Replace Only For a Specified Columns
df["Calories"].fillna(130, inplace = True)

#Replace Using Mean
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)

##Replace Using Median
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)

###Replace Using Mode
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)








