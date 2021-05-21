"""
Creates a file
f = open("Demofile.txt","x")
"""

"""
Writes on a file
f = open("Demofile.txt","w")
for i in range(10):
    f.write("Hello World!" + " This is line "+str(i+1)+"\n")
f.close()
"""

"""
Append values after the file element
g = open("Demofile.txt","a")
for i in range(5):
    f.write("Hello World!" + " This is appended line "+str(i+1)+"\n")
f.close()
"""

#Reads value from file
f = open("DemoFile.txt","r")

"""
READ ALL AT A TIME
contents = f.read()
print("contents",contents)
"""

"""
READ ALL LINE BY LINE
li = f.readlines()
for i in li:
    print(i)
"""


"""
READ SINGLE LINE 

print(f.readline(10))  ##105 bits
print(f.readline())
print(f.readline())

"""

"""
READ ALL LINE BY LINE
line = f.readline()
while line:
    print(line)
    line = f.readline()
"""

"""
READ FILE WITHOUT CALLING ANY FUNCTION
for x in f:
    print("new")
    print(x)
"""

"""
DELETE A FILE 
import os
os.remove("DemoFile.txt")

FIRT CHECK IF THE FILE EXITS
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

DELETE FOLDER
import os
os.rmdir("myfolder")
"""














