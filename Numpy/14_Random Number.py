from numpy import random

#random int
x = random.randint(100)     #randint => RANDom INTeger
print('Random Int: ', x)

#Random Float
x = random.rand()       #Ranndom Float
print('Random Float: ', x)

#Random Int Array
x=random.randint(100, size=(5)) #Ranndom 1-D Array with 5 element from 0 to 100 
print('Random Array: ', x)

x = random.randint(100, size=(3, 5))        #Ranndom 2-D Array with 3 rows and 5 columns from 0 to 100 
print(x)

#arndom Float Array
x = random.rand(3, 5)       #Generate a 2-D array with 3 rows, each row containing 5 random numbers
print("Floating Array: \n", x)

#Generate Random Number From Array
x = random.choice([3, 5, 7, 9], size = (3, 5))     #Choice from the Array
print(x)








