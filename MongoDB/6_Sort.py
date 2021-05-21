import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#Sort the Result
mydoc = mycol.find().sort("name")

print('Result Sorting with name:')
for x in mydoc:
  print(x)

#Sort Descending
#sort("name", 1) #ascending &&& sort("name", -1) #descending
mydoc = mycol.find().sort("name", -1)

print('\nResult Sorting with name in Descending order:')
for x in mydoc:
  print(x)










