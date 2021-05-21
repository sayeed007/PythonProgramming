import matplotlib.pyplot as plt
import seaborn as sns

print(sns.__version__)
arr = [0, 1, 2, 3, 4, 5]
sns.distplot(arr, hist = False)      #without the histogram

plt.show()















