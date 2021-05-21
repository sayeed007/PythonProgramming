n = int(input())
A = set(map(int,input().split()))

N = int(input())

for i in range(N):
    p = input().split()
    
    if p[0] == "intersection_update":
        B = set(map(int,input().split()))[:p[1]]
        A.intersection_update(B)

    elif p[0] == "update":
        B = set(map(int,input().split()))[:p[1]]
        A.update(B)
    elif p[0] = "symmetric_difference_update":
        B = set(map(int,input().split()))[:p[1]]
        A.symmetric_difference_update(B)
    elif p[0] = " difference_update":
        B = set(map(int,input().split()))[:p[1]]
        A.difference_update(B)

print (sum(A))
