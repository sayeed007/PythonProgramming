from itertools import permutations


S = input().split()
perM = permutations( S[0], int(S[1]) )

for i in sorted(perM):
    print (''.join(i))














