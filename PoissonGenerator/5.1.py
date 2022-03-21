import numpy as np
import math
import matplotlib.pyplot as plt


def PoissonGenerator(yn, lam):
    k = []
    j = 0

    while j != yn:
        q = np.exp(-lam)
        yk = 0
        ys = q
        yp = q
        u = np.random.uniform(0, 1)
        while u > ys:
            yk += 1
            yp = (yp*lam)/yk
            ys += yp
        k.append(yk)
        j += 1
    return k


def teoria(lam):
    t = []
    q = np.exp(-lam)

    for k in range(20):
        z = (pow(lam, k)/math.factorial(k))*q
        t.append(z)
    return t


x = np.arange(20)
plt.hist(PoissonGenerator(1000, 4), bins=12, density=True, color='lightblue',
         edgecolor='darkblue', label="Algorytm z wykładu")
plt.plot(teoria(4), '--')
plt.plot(x, teoria(4), "bo", label="Funkcja teoretyczna")
plt.legend()


plt.show()
