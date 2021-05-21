from itertools import combinations

io = input().split()
S = sorted(io[0])
k = int(io[1])

for i in range(1,k+1):
    for j in combinations(S,i):
        print("".join(j))