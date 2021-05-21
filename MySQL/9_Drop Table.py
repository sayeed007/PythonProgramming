import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'mydatabase'
)
mycursor = mydb.cursor()

sql = "SHOW TABLES"
mycursor.execute(sql)

for x in mycursor:
  print(x)

#Drop Only if Exist
print('Drop Only if Exist')

sql = "DROP TABLE IF EXISTS customers3" ##If table not exists, never create an error

mycursor.execute(sql)
myresult = mycursor.fetchall()

print(myresult)

#Delete a Table
print('Drop a table')

sql = "DROP TABLE customers2"   #If table not exists create an error

mycursor.execute(sql)
myresult = mycursor.fetchall()

print(myresult)











