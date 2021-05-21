import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


#Find One => The find_one() method returns the first occurrence in the selection.
x = mycol.find_one()
print(x)

#Find All
for x in mycol.find():
  print(x)

#Return Only Some Fields
#You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field).
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print('Return Only Some Fields', x)

#This example will exclude "address" from the result
for x in mycol.find({},{ "address": 0 }):
  print('Showing Result Except Address VAalues', x)







