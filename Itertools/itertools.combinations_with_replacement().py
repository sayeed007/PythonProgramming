from itertools import combinations_with_replacement

S = input().split()
st = ''.join(sorted(S[0]))

perM = combinations_with_replacement( st, int(S[1]) )

for i in perM:
    print (''.join(i))


