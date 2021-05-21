import pandas as pd
import numpy as np

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

std = np.std(full_health_data)

print("Standard Deviation of the data:", std)





#Coefficient of Variation
cv = np.std(full_health_data) / np.mean(full_health_data)
print("Coefficient of Variation: ", cv)
