import numpy as np 
from math import factorial
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)
y = np.zeros(len(x))

figure = plt.figure()

for n in range(0,10):
    taylorCoeff = (-1)**n * x**(2*n + 1)/factorial(2*n + 1) # Taylor coefficient/generalised term
 
    y = np.add(y, taylorCoeff)
    figure.clear()

    axis = figure.subplots()
    axis.plot(x,y)
    axis.set_xlabel('x')
    axis.set_ylabel('sin(x)') # Function here e.g. sin(x)
    axis.set_title('Terms :{}'.format(n+1))

    plt.xlim(min(x), max(y))
    plt.ylim(-2,2)
    plt.grid()
    plt.draw
    plt.pause(0.05)

print(y)
plt.show()
