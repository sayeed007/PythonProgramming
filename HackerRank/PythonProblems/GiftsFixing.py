t = int(input())

final = []

for i in range(t):
    n = int(input())
    a1 = list(map(int,input().split()))[:n]
    a2 = list(map(int,input().split()))[:n]

    if(len(a1) == len(a2)):
        min1 = min(a1)
        min2 = min(a2)

    count = 0

    for i in range(len(a1)):
        temp = int(a1[i]) - min1
        
        if temp > 0:
            count += temp

            if(min2 < int(a2[i])):
                if (int(a2[i]) - min2) >= temp:
                    a2[i] = str(int(a2[i]-temp))
                else:
                    a2[i] = str(min2)

    for i in range(len(a2)):
        temp = int(a2[i]) - min2
        if temp > 0:
            count += temp

    final.append(count)

for i in final:
    print(i) 



