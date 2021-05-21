from collections import Counter

X = int(input())
S = Counter(map(int,input().split()))
print(S)
print(type(S))
N = int(input()) 
earnings = 0

for customer in range(N):
    size, x_i = map( int,input().split() )
    if size in S.keys() and S[size] > 0:
        S[size] -= 1
        earnings += x_i
            
print(earnings)