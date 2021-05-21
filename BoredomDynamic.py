dp = []

n = int(input())

a = list(map(int,input().split()))[:n]

ar = []
for i in range(max(a)+1):
    ar.append(0)

for i in a:
    ar[i] += 1

dp.append(0)
dp.append(ar[1]) # a[1]*1 = a[1]

for i in range(2,len(ar)):
    dp.append(max(dp[i - 1], (dp[i - 2] + i*ar[i]) ) )

print(dp[-1])