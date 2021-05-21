import pymongo

#Creating mongodb Clint Object
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#Creating The Database
mydb = myclient["mydatabase"]

#Creating A Collection/ Same As Table
mycol = mydb["customers"]

        ###
        ### This code 
        ###

#can check if a collection exist in a database
print(mydb.list_collection_names())

#you can check a specific collection by name
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")




