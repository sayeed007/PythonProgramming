import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

#Check if Database Exists
print(myclient.list_database_names())

#check a specific database by name
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
else:
    print('No Such database found')












