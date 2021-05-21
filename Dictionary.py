n = int(input())
phonebook = dict()
for i in range(n):
    entry = str(input()).split(" ")

    name = entry[0]
    phone = int(entry[1])
    phonebook[name] = phone

while 1:
    try:
        q = input()
        if q in phonebook:
            print(str(q) + "=" + str(phonebook[q]))
        else:
            print("Not found")
    except:
        break