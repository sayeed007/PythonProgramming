n = int(input())
s1 = set(map(int,input().split()))

b = int(input())
s2 = set(map(int,input().split()))

x = s1.symmetric_difference(s2)

print(len(x))