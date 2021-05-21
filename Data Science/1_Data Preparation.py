import pandas as pd

health_data = pd.read_csv("data (1).csv", header=0, sep=",")
#header=0 means that the headers for the variable names are to be found in the first row (note that 0 means the first row in Python)
#sep="," means that "," is used as the separator between the values. This is because we are using the file type .csv (comma separated values)
print(health_data)