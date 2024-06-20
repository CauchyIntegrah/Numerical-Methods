import numpy as np              # Basic Numerical Derivative --> Variation of Mid-ordinate rule used for approximating integrals, but for derivatives
import matplotlib.pyplot as plt

def func(x,A,B):                            # Quadratic function defined here
    return A*x**2 + B*x

xList = np.linspace(0,10,100)
yList = func(xList,2,1,)
plt.plot(xList,yList,label="Function")

plt.axhline(color = 'black')
plt.axvline(color = 'black')

def D(xList,yList):                                     # Defining first numerical derivative
    yPrime = np.diff(yList)/np.diff(xList)                     # deltay/deltax
    xPrime = []                                         # Value of x for every value y'
    for i in range(len(yPrime)):
        xTemp = (xList[i+1]+xList[i])/2                 # Using midpoint node as a point to take numerical derivative - similar to Mid-ordinate rule for integration
        xPrime = np.append(xPrime,xTemp)
    return xPrime, yPrime

xPrime, yPrime = D(xList,yList)
plt.plot(xPrime,yPrime,label="Derivative")


xPrime2, yPrime2 = D(xPrime,yPrime)
plt.plot(xPrime2,yPrime2,label="2nd Derivative")       # y"

xPrime3, yPrime3 = D(xPrime2,yPrime2)
plt.plot(xPrime3,yPrime3,label="3rd Derivative")
plt.legend()




plt.show()
