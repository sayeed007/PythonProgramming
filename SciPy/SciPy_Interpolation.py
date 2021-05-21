from scipy.interpolate import interp1d
import numpy as np

#1D Interpolation
xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))
print("Normal 1D Interpolation\n", newarr)

#Spline Interpolation
from scipy.interpolate import UnivariateSpline
xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = UnivariateSpline(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))
print("Spline Interpolation\n", newarr)


#Interpolation with Radial Basis Function
from scipy.interpolate import Rbf

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = Rbf(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))
print("Interpolation with Radial Basis Function\n", newarr)
















