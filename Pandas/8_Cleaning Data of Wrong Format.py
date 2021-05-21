import pandas as pd

df = pd.read_csv('dirtydata.csv')

###Convert Into a Correct Format
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())


###Removing Rows
df['Date'] = pd.to_datetime(df['Date'])
df.dropna(subset=['Date'], inplace = True)
print(df.to_string())













