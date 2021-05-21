import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="mydatabase"
)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)


#ORDER BY DESC
print('\n\nUse the DESC keyword to sort the result in a descending order')
sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)
myresult = mycursor.fetchall()
print(mycursor)
for x in myresult:
  print(x)








