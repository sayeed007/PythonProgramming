import pandas as pd
import numpy as np

health_data = pd.read_csv("data.csv", header=0, sep=",")

x = health_data["Average_Pulse"]
y = health_data["Calorie_Burnage"]
slope_intercept = np.polyfit(x,y,1)
#returned function has 2 parameters 1.slope & 2.intercept
#The last parameter of the function specifies the degree of the function, which in this case is "1"

print(slope_intercept)