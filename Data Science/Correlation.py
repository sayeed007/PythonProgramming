import pandas as pd
import matplotlib.pyplot as plt

#Example of a Perfect Linear Relationship (Correlation Coefficient = 1)
plt.subplot(2,1,1)
health_data = pd.read_csv("data.csv", header=0, sep=",")
health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='scatter'),



#Example of a Perfect Negative Linear Relationship (Correlation Coefficient = -1)
negative_corr = {'Hours_Work_Before_Training': [10,9,8,7,6,5,4,3,2,1],
'Calorie_Burnage': [220,240,260,280,300,320,340,360,380,400]}
negative_corr = pd.DataFrame(data=negative_corr)
negative_corr.plot(x ='Hours_Work_Before_Training', y='Calorie_Burnage', kind='scatter')


#Example of No Linear Relationship (Correlation coefficient = 0)
health_data.plot(x ='Duration', y='Max_Pulse', kind='scatter')



plt.show()


