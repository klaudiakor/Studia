import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse.dia import dia_matrix
import scipy.sparse.linalg


def xi_point(i, n):
    return (-1)+(2*(i/n))


def fun(x):
    return 1/(1+25*(x**2))


def solve_Eq(N, h):
    ex = np.ones(N)
    data = np.array([ex, 4*ex, ex])
    offsets = np.array([-1, 0, 1])
    matrix = dia_matrix((data, offsets), shape=(N-1, N-1)).toarray()

    b = np.empty(N-1)
    for i in range(0, N-1):
        b[i] = (6/(h*h))*(fun(xi_point(i, N)) -
                          (2 * fun(xi_point(i+1, N))) + fun(xi_point(i+2, N)))

    k = scipy.sparse.linalg.lsqr(matrix, b)[:1]
    ksi = list(k[0])
    ksi.insert(0, 0)
    ksi.append(0)
    return ksi


def plot_fun():
    xf = np.linspace(-1, 1, 100)
    plt.plot(xf, fun(xf), '--', label="f(x)")
    plt.legend(loc="upper right")
    plt.title("Interpolacja naturalnymi splajnami kubicznymi")
    plt.show()


def yj(xp, j, x, ksi_vec):
    A = (x[j+1]-xp)/(x[j+1]-x[j])
    B = (xp-x[j])/(x[j+1]-x[j])
    C = ((A**3)-A)*(x[j+1]-x[j])**2/6
    D = ((B**3)-B)*(x[j+1]-x[j])**2/6

    return (A*fun(x[j]) + B*fun(x[j+1]) + C*ksi_vec[j] + D*ksi_vec[j+1])


def QubicSpline(x, N, ksi_vec):

    section_yplt = np.array([], float)
    xplt = np.array([], float)
    for j in range(0, N):
        start = x[j]
        stop = x[j+1]
        num = 10
        step = (stop-start)/num
        if j+1 == N:
            step = 0
        section_xplt = np.linspace(start, stop-step, num)
        for xi in section_xplt:
            section_yplt = np.append(section_yplt, yj(xi, j, x, ksi_vec))

        xplt = np.append(xplt, section_xplt)
    return (xplt, section_yplt)


def main(N):
    x = np.array([], float)

    for i in range(0, N+1):
        x = np.append(x, xi_point(i, N))

    h = x[1] - x[0]
    ksi_vec = solve_Eq(N, h)

    yplt = np.array([], float)
    xplt = np.array([], float)

    yplt = np.append(yplt, QubicSpline(x, N, ksi_vec)[1])
    xplt = np.append(xplt, QubicSpline(x, N, ksi_vec)[0])
    plt.plot(xplt, yplt, label="S"+str(N)+"(x)")

    return (xplt, yplt, x)


def sub(N):
    Qx = main(N)[0]
    Qy = main(N)[1]
    x = main(N)[2]
    y = np.zeros(len(x))
    yplt = np.array([], float)

    i = 0
    for xi in Qx:
        yplt = np.append(yplt, abs(fun(xi) - Qy[i]))
        i += 1

    plt.title("Błąd interpolacji splajnami kubicznymi")
    plt.xlabel("x")
    plt.ylabel("|f(x)-s(x)|")
    plt.plot(Qx, yplt, label="błąd interpolacji dla S"+str(N)+"(x)")
    plt.plot(x, y, 'o', label="węzły interpolacji")
    plt.legend(loc="upper right")


main(5)
main(6)
main(8)
main(10)
main(50)
plot_fun()
# sub(7)
# sub(55)
# plt.show()
