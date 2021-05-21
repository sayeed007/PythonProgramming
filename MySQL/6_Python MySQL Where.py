import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="mydatabase"
)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Ocean blvd 2'"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Wildcard Characters
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"  #address contains the word "way"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Prevent SQL Injection
#Escape query values by using the placholder %s method:
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)









