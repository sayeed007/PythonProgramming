import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#Filter the Result
myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

print('Finding data whose address => "Park Lane 38" ')
for x in mydoc:
  print(x)

#Advanced Query
myquery = { "address": { "$gt": "S" } }
#Find documents where the address starts with the letter "S" or higher

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

#Filter With Regular Expressions
#To find only the documents where the "address" field starts with the letter "S", use the regular expression {"$regex": "^S"}
myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

print("\nExample of Regular Expressions")
for x in mydoc:
  print(x)

















