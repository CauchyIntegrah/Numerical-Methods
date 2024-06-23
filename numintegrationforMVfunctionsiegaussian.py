# More numerical integration

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import nquad
from scipy.special import erf

def f(z,y,x,a):
    return np.exp(-a*(x**2 + y**2 + z**2))

rangeX = [0,1]
rangeY = [0,1]
rangeZ = [0,1]

def I_1s(a):
    return nquad(f, [rangeZ, rangeY, rangeX] ,args = (a,))

#aval = np.linspace(eps,5, 10)
#I_1s(aval)[1]
# ^ This won't work, as this integral wants a scalar argument, and we have given it an array of values.
I_1 = np.vectorize(I_1s)

def ans(a):
    prop = (np.pi/(4*a)**(3/2))
    return prop*erf(np.sqrt(a))**3

eps = 1.0e-6
avals = np.linspace(eps, 10, 15)

def rangeZZ(y,x,a):
    return [0,1-x-y]

def rangeYY(x,a):
    return [0, 1-x]

rangeXX = [0,1]

def I_2s(a):
    return nquad(f, [rangeZZ, rangeYY, rangeXX] ,args = (a,))

I_2 = np.vectorize(I_2s)


#Plotting
plt.plot(avals, I_1(avals)[0], label = "SI_1(a)-Numeric" , linestyle = "--", color = "black")

plt.plot(avals, I_2(avals)[0], label = "SI_2(a)-Numeric" , linestyle = "--", color = "red")


plt.plot(avals, ans(avals), label = "SI_1(a)-Analytic" , linestyle = ":", color = "blue", linewidth = 7)
plt.title("Same number, except I2")
plt.legend()
plt.grid()
plt.xlabel('a')
plt.show()
