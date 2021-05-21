import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')


###Plotting
df.plot()

###Scatter Plot
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

###Bad Co-relation
df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show()
###Histogram
df["Duration"].plot(kind = 'hist')




plt.show()


















