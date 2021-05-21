import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(type(y))


#Convert From Python to JSON:
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print(type(y))

#ython objects of the following types, into JSON strings:

print(json.dumps({"name": "John", "age": 30}))  #dict  -> json(Object)
print(json.dumps(["apple", "bananas"]))         #list  -> json(Array)
print(json.dumps(("apple", "bananas")))         #tuple -> json(Array)
print(json.dumps("hello"))                      #str   -> json(String)
print(json.dumps(42))                           #int   -> json(number)
print(json.dumps(31.76))                        #float -> json(Number)
print(json.dumps(True))                         #bool  -> json(true)
print(json.dumps(False))                        #bool  -> json(false)
print(json.dumps(None))                         #null  -> json(null)



x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, sort_keys=True))
