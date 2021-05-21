from typing import OrderedDict

n = int(input())

d = OrderedDict()


for i in range(n):
    st = input()
    p = d.keys()
    
    if st in p:
        d[st] += 1
    else:
        d[st] = 1

print(len(d.keys()))
for i in d.keys():
    print (d[i], end = " ")






'''
a = 'abcdef'
b = 'bcd'

if b in a:
    print("done")
'''

