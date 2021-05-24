# Complete the birthday function below.
def birthday(s, d, m, n):
    total = 0
    count = 0
    for i in range(n-m+1):
        total = 0
        for j in range(i,i+m):
            total += s[j]
            print("total=" ,total)
        if(total == d):
            count += 1
            print("count=" ,count)
    
    return count


n = 1

s = [4]

d = 4  #total value

m = 1  #continuous bars
S
result = birthday(s, d, m, n)

print(result)
