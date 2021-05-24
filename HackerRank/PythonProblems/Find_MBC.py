import cmath
import math

ab = int(input())
bc = int(input())

print (str(int(round(math.degrees(cmath.phase(complex(bc,ab))))))+'')