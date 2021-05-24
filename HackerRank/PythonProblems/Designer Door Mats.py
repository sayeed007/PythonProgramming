x, y = map(int,input().split())
print(type(x))
mid = (x // 2) + 1
mid2 = ((y // 2) - 1)
c = ".|."
d = "-"

x = mid2
#UPPER HALF
for i in range(mid-1):
    print((d*x)+c+(2*i*c)+(d*x))
    x -= 3

x = mid2-2
#MIDDLE
print((d*x)+"WELCOME"+(d*x))

#LOWER HALF
x = 3
#UPPER HALF
for i in range(mid-2,-1,-1):
    print((d*x)+c+(2*i*c)+(d*x))
    x += 3

