import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'mydatabase'
)
mycursor = mydb.cursor()

#ou can limit the number of records returned from the query, by using the "LIMIT" statement
mycursor.execute("SELECT * FROM customers LIMIT 5")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Start From Another Position
print('Followings are records starting with 3th position and then 3 values')
mycursor.execute("SELECT * FROM customers LIMIT 3 OFFSET 2")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)










