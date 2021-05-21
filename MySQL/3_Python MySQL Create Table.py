import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="mydatabase"
)
mycursor = mydb.cursor()

#Creating Data Table
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#If the table already exists, use the ALTER TABLE keyword:
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


#Create primary key when creating the table
#mycursor.execute("CREATE TABLE customers2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#Check if Table Exists
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)








