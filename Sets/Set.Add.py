# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
stamp = []

for i in range(N):
    x = str(input())
    stamp.append(x)

s = set(stamp)
print(len(s))
