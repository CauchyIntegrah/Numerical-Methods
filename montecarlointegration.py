import random
import numpy as np
import matplotlib.pyplot as plt
aLimit = 0
bLimit = np.pi # Limits of integration
N = 1000
xRand = np.zeros(N)
for i in range(len(xRand)):
    xRand[i] = random.uniform(aLimit,bLimit)

def func(x):
    return np.sin(x)
integral = 0.0
for i in range(N):
    integral += func(xRand[i])

answer = (bLimit-aLimit)/float(N)*integral
print("The integral from 0 to pi of sin(x): ", answer)
