import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'mydatabase'
)
mycursor = mydb.cursor()
'''
sql  = "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav VARCHAR(255))"
sql2 = "CREATE TABLE products (id VARCHAR(255), name VARCHAR(255))"

mycursor.execute(sql)
mycursor.execute(sql2)


#INSERT into users table
sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
val = [
  ('John', '154'),
  ('Peter', '154'),
  ('Amy', '155'),
  ('Hannah', '153'),
  ('Michael', '156')

]
mycursor.executemany(sql, val)
mydb.commit()

#INSERT into products table
sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
val = [
  ('154', 'Chocolate Heaven'),
  ('155', 'Tasty Lemons' ),
  ('156', 'Vanilla Dreams') 
]
mycursor.executemany(sql, val)
mydb.commit()
'''
#Viewing table
mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchall()

print('Table users:')
for x in myresult:
  print(x)

mycursor.execute("SELECT * FROM products")
myresult = mycursor.fetchall()

print('Table products:')
for x in myresult:
  print(x)

#Join Two or More Tables
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()

print('\nJoin two table where users.fav = products.id')
for x in myresult:
    print(x)

#LEFT JOIN
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()

print('\nLeft Join two table where users.fav = products.id')
for x in myresult:
    print(x)

#RIGHT JOIN
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()

print('\nRight Join two table where users.fav = products.id')
for x in myresult:
    print(x)















