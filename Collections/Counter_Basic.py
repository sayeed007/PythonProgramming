from collections import Counter

X = int(input())    #Number of Shoes
li = list( map (int,input().split()))

N = int(input())    #Number of customers

total = 0

for i in range(N):
    size, price =  map( int,input().split())
    if size in li:
        total += price
        li.remove(size)
print(total)



