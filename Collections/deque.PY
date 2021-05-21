from collections import deque

N = int(input())
d = deque()

for i in range(N):
    s = input().split()

    if s[0] == 'append':
        d.append( int(s[1]) ) 
    elif s[0] == 'appendleft':
        d.appendleft( int(s[1]) )
    elif s[0] == 'pop':
        d.pop()
    elif s[0] == 'popleft':
        d.popleft()

for i in d:
    print(i, end = ' ')

