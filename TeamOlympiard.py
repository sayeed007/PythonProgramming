n = int(input())

t = list(map(int,input().split()))[:n]

one =  []
two =  []
three =  []

for i in range(n):
    if (t[i] <= 1):
        one.append(i+1)
    elif (t[i] >= 3):
        three.append(i+1)
    else:
        two.append(i+1)  

w = min(len(one),len(two),len(three))
print(w)
for i in range(w):
    print(one[i],two[i],three[i])