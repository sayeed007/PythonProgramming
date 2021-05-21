from collections import defaultdict

n, m = map( int,input().split() )

d = defaultdict(list)


for i in range(n):      #group A values
    x = input()
    d[x].append( str(i+1) )

print(d)

for i in range(m):
    y = input()
    print(' '.join(d[y]) or -1)