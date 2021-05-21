import re
#The findall() function returns a list containing all matches.
txt = "The rain in Spain"
#[]	A set of characters	"[a-m]"
x = re.findall("[a-m]", txt)
print(x)

#Find all digit characters:
txt2 = "That will be 59 dollars"
x = re.findall("\d", txt2)
print(x)

#Check if the string starts with 'hello':
x = re.findall("^hello", txt) #can replaced by \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
print(x)

#Check if the string ends with 'world':
x = re.findall("pain$", txt)
print(x)


#The search() function searches the string for a match, and returns a Match object if there is a match.

txt = "The rain in Spain"
x = re.search("\s", txt) #string contains a white space character
print("The first white-space character is located in position:", x.start())


txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x) #return None

#The split() function returns a list where the string has been split at each match
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 1) #Split the string only at the first occurrence:
print(x)

#The sub() function replaces the matches with the text of your choice
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)#Space replaced by 9
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)#replace only for 1st 2 occurance
print(x)




