def possible( m,  s):
    if (s >= 0) and (s <= 9 * m):
        return True
    else:
        return False

#MAIN FUNCTION
m, summation = map(int,input().split())
summ = summation
minn = ""
maxx = ""

for pos in range(m):
    for digit in range(10):
        if(  (pos > 0 or digit > 0 or (m == 1 and digit == 0)) 
            and possible(m - pos - 1, summ - digit)  ):
            minn += (str(digit))
            summ -= digit
            break

summ = summation
for pos in range(m):
    for digit in range(9,-1,-1):
        if(possible(m - pos - 1, summ - digit)):
            maxx += (str(digit))
            summ -= digit
            break

if((summation <= 0 and m > 1) or (summation > 9 * m)):
    maxx = minn = -1
    
print(minn,maxx)