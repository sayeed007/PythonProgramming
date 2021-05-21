import pandas as pd
import numpy as np

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

print (full_health_data.describe())


#Task: Find the 10% percentile for Max_Pulse
Max_Pulse= full_health_data["Max_Pulse"]
percentile10 = np.percentile(Max_Pulse, 10)
print("Percentile of 10% = ", percentile10)




