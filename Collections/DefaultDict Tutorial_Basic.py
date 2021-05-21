n, m = map( int,input().split() )
A = []
for i in range(n):      #group A values
    x = input()
    A.append(x)

B = []
for i in range(m):
    y = input()
    B.append(y)

lis = []

for i in B:
    lis = []
    for j in range( len(A) ):
        if i == A[j]:
            lis.append(j+1)
    if len(lis) == 0:
        lis.append(-1)
    for p in lis:
        print(p, end = " ")
    print()







