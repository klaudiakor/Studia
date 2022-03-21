# autor: Klaudia Korczak
# zadanie numeryczne 1

import matplotlib.pyplot as plt
import numpy as np


def F(arg):
    # zadana funkcja
    return np.cos(arg)


def dF(arg):
    # pochodna z zadanej funkcji
    return -np.sin(arg)


def funA(x, h, F):
    # wzor na pochodna z podpunktu (a)
    return (F(x+h)-F(x))/h


def funB(x, h, F):
    # wzor na pochodna z podpunktu (b)
    return (F(x+h)-F(x-h))/(2*h)


def E_a(x, h, F, dF):
    # błąd dla podpunktu a
    return np.abs(funA(x, h, F) - dF(x))


def E_b(x, h, F, dF):
    # błąd dla podpunktu b
    return np.abs(funB(x, h, F) - dF(x))


h_64 = np.logspace(-17, 0, num=80, dtype=np.float64)
h_32 = np.logspace(-17, 0, num=80, dtype=np.float32)
x = 0.3

# wykres dla podpunktu A
plt.subplot(1, 2, 1)
plt.title("A")
plt.yscale('log')
plt.xscale('log')
plt.plot(h_64, E_a(x, h_64, F, dF), label="binary64")
plt.plot(h_32, E_a(x, h_32, F, dF), linestyle="--", label="binary32")
plt.legend(loc="lower left")
plt.ylabel('log(E)')
plt.xlabel('log(h)')

# wykres dla podpunktu B
plt.subplot(1, 2, 2)
plt.title("B")
plt.yscale('log')
plt.xscale('log')
plt.plot(h_64, E_b(x, h_64, F, dF), label="binary64")
plt.plot(h_32, E_b(x, h_32, F, dF), linestyle="--", label="binary32")
plt.legend(loc="lower left")
plt.ylabel('log(E)')
plt.xlabel('log(h)')

plt.show()
