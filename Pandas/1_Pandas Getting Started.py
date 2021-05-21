import pandas as pd

#Checking Pandas Version
print("pandas",pd.__version__,"is currently running")

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
