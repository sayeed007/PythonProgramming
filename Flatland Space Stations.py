import math

n,m = map(int,input().split())
c= sorted(map(int,input().split()))
m = max(n-c[-1]-1,c[0])
for i in range(1,len(c)):
    d = math.floor((c[i]-c[i-1])/2)
    if d>m:
        m=d
print(m)