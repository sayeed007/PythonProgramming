import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#delete_one() => If the query finds more than one document, only the first occurrence is deleted
myquery = { "address": "Mountain 21" }

print("Delete first data with address => Mountain 21")
mycol.delete_one(myquery)

#Delete Many Documents
myquery = { "address": {"$regex": "^S"} }

#Delete all documents were the address starts with the letter S:
x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")

#Delete All Documents in a Collection
x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")






















