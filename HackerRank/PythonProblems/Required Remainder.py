t = int(input())

final = []
for i in range(t):
    x, y, n = map(int,input().split())

    p = n % x

    if p == y:
        k = n

    elif p < y:
        p = p + x
        q = p - y
        k = n - q
    else:
        q = p - y
        k = n - q

    final.append(k)

for i in final:
    print(i)