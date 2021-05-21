import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="mydatabase"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Selecting Columns
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()

print('Using columns Selection method:')
for x in myresult:
  print(x)

#Using the fetchone() Method
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()

print('First element value of the database: \n', myresult)



















