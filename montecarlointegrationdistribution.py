import random
import numpy as np
import matplotlib.pyplot as plt
aLimit = 0
bLimit = np.pi # Limits of integration
N = 1000
xRand = np.zeros(N)


def func(x):
    return np.sin(x)


areas = []

for i in range(N):
    xRand = np.zeros(N)
    for i in range(len(xRand)):
        xRand[i] = random.uniform(aLimit,bLimit)
        integral = 0.0
    for i in range(N):
        integral += func(xRand[i])

    answer = (bLimit-aLimit)/float(N)*integral

    areas.append(answer)
plt.title("Distribution of Areas Calculated")
plt.hist(areas,bins = 30, ec = 'black')
plt.xlabel("Areas")
plt.show()
