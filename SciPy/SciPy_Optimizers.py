from scipy.optimize import root
from math import cos

print("Optimizers are a set of procedures defined in SciPy \nthat either find the minimum value of a function, or the root of an equation.")
print("\nNumPy is capable of finding roots for polynomials and linear equations")
def eqn(x):
  return x + cos(x)

#The returned object has much more information about the solution.
myroot = root(eqn, 0)
#eqn - a function representing an equation.
#x0 - an initial guess for the root.
print(myroot.x)
print(myroot)

#Finding Minima
print("\nMinimize the function x^2 + x + 2 with BFGS:")
from scipy.optimize import minimize

def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')

print(mymin)

























