t = int(input())

out = []

for i in range(t):
    n = int(input())
    temp = 99999999999
    s = list(map(int,input().split()))[:n]
    s.sort()

    for i in range(1,n):
        if(s[i]-s[i-1] <= temp):
            temp = s[i]-s[i-1]
    out.append(temp) 

for i in out:
    print(i)
