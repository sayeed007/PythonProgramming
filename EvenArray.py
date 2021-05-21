def find(a):
    tempO = []
    tempE = []

    for i in range(len(a)):
        if (i%2 == 0):
            if (a[i]%2 != 0):
                tempE.append(i)

        else:
            if (a[i]%2 == 0):
                tempO.append(i)
    O = len(tempO)
    E = len(tempE)
    if (O == E):
        return (max(O,E))
    else:
        return -1
        




#Drive Code
t = int(input())
result = []

for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    result.append(find(arr))
for i in result:
    print(i)