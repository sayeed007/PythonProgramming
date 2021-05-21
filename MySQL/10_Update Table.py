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
print('Following tables are available in the databases:')
for x in mycursor:
  print(x)

#ou can update existing records in a table by using the "UPDATE" statement:
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

#Prevent SQL Injection
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")







