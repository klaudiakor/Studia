import matplotlib.pyplot as plt
import numpy as np


def y1(x):
    return 1/(1+25*x**2)


def y2(x):
    return 1/(1+x**2)


def a(i, N):
    return ((2*i)/(N))-1


def b(i, N):
    return np.cos((2*i+1)/(2*(N+1))*np.pi)


def Interpolation(xp, X, Y, N):
    yp = 0
    for i in range(N):
        p = 1
        for j in range(N):
            if i != j:
                p *= (xp-X[j])/(X[i]-X[j])

        yp += p * Y[i]
    return yp


def plotA(N, fun):
    xa = np.array([], float)
    ya = np.array([], float)

    for ai in range(0, N+1):
        xa = np.append(xa, a(ai, N))

    xaplt = np.linspace(xa[0], xa[-1], 300)
    yaplt = np.array([], float)

    for xi in xa:
        ya = np.append(ya, fun(xi))

    for xp in xaplt:
        yaplt = np.append(yaplt, Interpolation(xp, xa, ya, N+1))

    plt.plot(xaplt, yaplt, label="W"+str(N)+" dla a)")
    plt.xlabel('x')
    plt.ylabel('y')


def plotB(N, fun):
    x = np.array([], float)
    y = np.array([], float)

    for i in range(0, N+1):
        x = np.append(x, b(i, N))

    xaplt = np.linspace(x[0], x[-1], 300)
    yaplt = np.array([], float)

    for xi in x:
        y = np.append(y, fun(xi))

    for xp in xaplt:
        yaplt = np.append(yaplt, Interpolation(xp, x, y, N+1))

    plt.plot(xaplt, yaplt, label="W"+str(N)+" dla b)")
    plt.xlabel('x')
    plt.ylabel('y')


def plot_fun1():
    xf = np.linspace(-1, 1, 300)
    plt.plot(xf, y1(xf), label="funkcja 1")
    plt.legend(loc="upper right")
    plt.show()


def plot_fun2():
    xf = np.linspace(-1, 1, 300)
    plt.plot(xf, y2(xf), label="funkcja 2")
    plt.legend(loc="upper right")
    plt.show()


plt.title("Wielomiany interpolacyjne dla funkcji: y(x) = 1/(1+25x^2)\ni węzłów interpolacji: xi = -1+2i/n")
plotA(10, y1)
plotA(5, y1)
plotA(7, y1)
plot_fun1()

plt.title("Wielomiany interpolacyjne dla funkcji: y(x) = 1/(1+25x^2)\ni węzłów interpolacji: xi = cos((2i+1)/(2(n+1))pi)")
plotB(17, y1)
plotB(7, y1)
plotB(5, y1)
plot_fun1()


plt.title("Wielomiany interpolacyjne dla funkcji: y(x) = 1/(1+x^2)\ni węzłów interpolacji: xi = -1+2i/n")
plotA(10, y2)
plotA(5, y2)
plotA(7, y2)
plot_fun2()

plt.title("Wielomiany interpolacyjne dla funkcji: y(x) = 1/(1+x^2)\ni węzłów interpolacji: xi = cos((2i+1)/(2(n+1))pi)")
plotB(17, y2)
plotB(7, y2)
plotB(5, y2)
plot_fun2()
