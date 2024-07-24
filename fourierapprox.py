import numpy as np 
import matplotlib.pyplot as plt

figure = plt.figure(figsize=(8,4.125))
L = np.pi

xVec = np.linspace(-L, L, 500)
yVec = xVec # Test function (f(x) = x)

a_0 = 1/L * np.trapz(yVec, xVec, dx = 1/100)

yFourier = np.zeros(len(xVec)) + a_0/2

for n in range(1, 1000):
    figure.clear()
    # Plotting
    axis = figure.subplots()
    axis.plot(xVec, yFourier, color = 'black', label = 'Fourier Approx.')
    axis.plot(xVec, yVec, '--', color = 'blue', label = 'Periodic Function')

    axis.set_title(f'Approximation of y = x with Fourier having {n} terms.')
    axis.set_xlabel('x')
    axis.set_ylabel('f(x) - Using Fourier')
    plt.xlim(1.2*min(xVec), 1.2*max(xVec))
    plt.ylim(1.2*min(yVec), 1.2*max(yVec))
    plt.grid()
    plt.legend()
    plt.draw()
    plt.pause(0.05)
    #Fourier Coefficient/Term
    a_n = 1/L * np.trapz(yVec*np.cos(np.pi*n*xVec/L), xVec, dx = 1/100) # Trapezoid Method of Numerical Integration
    b_n = 1/L * np.trapz(yVec*np.sin(np.pi*n*xVec/L), xVec, dx = 1/100)

    
    fourierCoeff = a_n*np.cos(np.pi*n*xVec/L) + b_n*np.sin(np.pi*n*xVec/L)

    yFourier = np.add(fourierCoeff, yFourier)
