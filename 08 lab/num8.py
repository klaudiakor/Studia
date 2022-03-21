import numpy as np
from scipy import integrate

# epsilon = 1E-9
epsilon = 0.001


# functions


def f1(x, p): return np.sin(x)


def f2(x, y):
    return np.log(x**2+y**3+1)


# Granice całkowania
a = 0
b = 1


def Trap(f, n, a, b, param):  # metoda trapezów
    h = (b-a)/n  # number of segments
    sum = 0
    for i in range(1, n):
        sum = sum + 2 * f(a+i*h, param)
    trap = (h/2)*(f(a, param)+sum+f(b, param))
    return trap


def Integrate_Romberg(f, a, b, param):  # metoda Romberga
    T = np.zeros((10, 10))
    eps = 100
    n = 1
    i = 1
    T[1, 1] = Trap(f, n, a, b, param)

    while eps > epsilon:
        # zwiększam liczbę trapezów
        n = 2**i

        # kolejne przybliżenie całki
        T[i+1, 1] = Trap(f, n, a, b, param)

        # całka romberga
        for k in range(2, i+2):
            j = 2+i-k
            T[j, k] = (4**(k-1)*T[j+1, k-1]-T[j, k-1])/(4**(k-1)-1)

        # bieżący epsilon
        eps = abs(T[1, i+1] - T[2, i])

        # dla następnej iteracji
        i += 1

    return T[1, i]


def Integrate_NC(f, a, b, param):  # kwadratura Newtona-Cotesa (wzór Simpsona)
    eps = 100
    n = 2
    old = 100
    ii = 1

    while eps > epsilon:
        # ilość przedziałów
        h = (b-a)/n

        sum1 = 0
        for i in range(1, n, 2):
            sum1 += 4*f(a+i*h, param)
            print("sum1 ", ii, i, a+i*h)

        sum2 = 0
        for i in range(2, n-1, 2):
            sum2 += 2*f(a+i*h, param)
            print("sum2 ", ii, i, a+i*h)

        # obliczanie przybliżenia całki
        integral = (h/3)*(f(a, param)+sum1+sum2+f(b, param))

        # bieżący epsilon
        eps = abs((integral - old)/integral)*100

        # dla kolejnej iteracji
        old = integral
        n += 2
        ii += 1

    return integral


print("Całka (a):")
print("Funkcja biblioteczna: ", integrate.quad(lambda x: np.sin(x), 0, 1))
print("Metoda Romberga: ", Integrate_Romberg(f1, a, b, 0))
print("Wzór Simpsona: ", Integrate_NC(f1, a, b, 0))
print()


# steps = 1000
# y_points = np.linspace(a, b, steps)
# width = abs(b - a) / steps
# res_r = 0
# res_s = 0
# for y in y_points:
#     res_r += (Integrate_Romberg(f2, a, b, y) * width)
#     res_s += Integrate_NC(f2, a, b, y) * width

# print("Całka (b):")
# print("Funkcja biblioteczna: ", integrate.nquad(f2, [[0, 1], [0, 1]]))
# print("Metoda Romberga: ", res_r)
# print("Wzór Simpsona: ", res_s)
