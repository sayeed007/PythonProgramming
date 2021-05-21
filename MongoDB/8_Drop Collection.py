import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

print(mycol.drop() )
#The drop() method returns true if the collection was dropped successfully, and false if the collection does not exis

