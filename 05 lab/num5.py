import numpy as np
import matplotlib.pyplot as plt

N = 100
maxiter = 200
tolerance = 1e-9
exact_x = []

ay_jacobi = []
ax_jacobi = []
ay_gauss = []
ax_gauss = []


def mxA(row, column):
    if row == column:
        return 3
    elif row == column + 1 or row == column - 1:
        return 1
    elif row == column + 2 or row == column - 2:
        return 0.2
    else:
        return 0


def vecB(row):
    return row+1


def ExactSolution():
    mx_str = ''
    for i in range(N):
        for j in range(N):
            mx_str += str(mxA(i, j)) + ' '
        if not i == N-1:
            mx_str += ';'

    mx = np.matrix(mx_str)

    b = np.empty(N)
    for k in range(0, N):
        b[k] = k+1

    x = np.linalg.solve(mx, b)
    return x


exact_x = ExactSolution()


def Jacobi():
    x0 = np.zeros(N)
    # x0 = np.empty(N)
    # x0.fill(10)
    x_prev = x0.copy()

    for i in range(maxiter):
        x = x0.copy()
        x[0] = (vecB(0) - mxA(0, 1) * x_prev[1] -
                mxA(0, 2) * x_prev[2])/mxA(0, 0)
        x[1] = (vecB(1) - mxA(1, 0) * x_prev[0] - mxA(1, 2)
                * x_prev[2] - mxA(1, 3)*x_prev[3])/mxA(1, 1)

        for j in range(2, N-2):
            x[j] = (vecB(j) - mxA(j, j-2)*x_prev[j-2] - mxA(j, j-1)*x_prev[j-1] -
                    mxA(j, j+1)*x_prev[j+1]-mxA(j, j+2)*x_prev[j+2])/mxA(j, j)

        x[N-2] = (vecB(N-2) - mxA(N-2, N-4)*x_prev[N-4] - mxA(N-2, N-3)
                  * x_prev[N-3] - mxA(N-2, N-1)*x_prev[N-1])/mxA(N-2, N-2)
        x[N-1] = (vecB(N-1) - mxA(N-1, N-3) * x_prev[N-3] -
                  mxA(N-1, N-2) * x_prev[N-2])/mxA(N-1, N-1)

        # norm = 0
        # for k in range(0, N):
        #     norm += (x[k] - x_prev[k]) ** 2
        # norm = np.sqrt(norm)

        norm = np.linalg.norm(x-x_prev)

        if norm < tolerance:
            break

        x_prev = x

        ay_jacobi.append(np.linalg.norm(x-exact_x))
        ax_jacobi.append(i)

    if norm > tolerance:
        print(
            "[EXCEPTION]: Ciąg jest wolno zbieżny. Ilość wykonanych iteracji: ", maxiter)
    print("METODA JACOBIEGO")
    print("Ilość wykonanych iteracji: ", i)
    return x_prev


def GaussSaidel():
    x0 = np.zeros(N)
    # x0 = np.empty(N)
    # x0.fill(10)
    x_prev = x0.copy()

    for i in range(maxiter):
        x = x0.copy()
        x[0] = (vecB(0) - mxA(0, 1) * x_prev[1] -
                mxA(0, 2) * x_prev[2])/mxA(0, 0)
        x[1] = (vecB(1) - mxA(1, 0) * x[0] - mxA(1, 2)
                * x_prev[2] - mxA(1, 3)*x_prev[3])/mxA(1, 1)

        for j in range(2, N-2):
            x[j] = (vecB(j) - mxA(j, j-2)*x[j-2] - mxA(j, j-1)*x[j-1] -
                    mxA(j, j+1)*x_prev[j+1]-mxA(j, j+2)*x_prev[j+2])/mxA(j, j)

        x[N-2] = (vecB(N-2) - mxA(N-2, N-4)*x[N-4] - mxA(N-2, N-3)
                  * x[N-3] - mxA(N-2, N-1)*x_prev[N-1])/mxA(N-2, N-2)
        x[N-1] = (vecB(N-1) - mxA(N-1, N-3) * x[N-3] -
                  mxA(N-1, N-2) * x[N-2])/mxA(N-1, N-1)

        norm = np.linalg.norm(x-x_prev)

        if norm < tolerance:
            break

        x_prev = x

        ay_gauss.append(np.linalg.norm(x-exact_x))
        ax_gauss.append(i)

    if norm > tolerance:
        print(
            "[EXCEPTION]: Ciąg jest wolno zbierzny. Ilość wykonanych iteracji: ", maxiter)

    print("METODA GAUSSA-SAIDELA")
    print("Ilość wykonanych iteracji: ", i)
    return x_prev


def latex(w):
    res = r"\begin{pmatrix}"
    for _ in range(0, 50):
        res += str(w[_])
        if _ != N-1:
            res += r"\\"
    res += r"\end{pmatrix}"
    res2 = r"\begin{pmatrix}"
    for _ in range(50, N):
        res2 += str(w[_])
        if _ != N-1:
            res2 += r"\\"
    res2 += r"\end{pmatrix}"
    print(res+res2)


j_x = Jacobi()
# print(j_x)
# latex(j_x)
g_x = GaussSaidel()
# latex(g_x)
# print(g_x)
#print("DOKŁADNE ROZWIĄZANIE")
# print(exact_x)

plt.yscale('log')
plt.plot(ax_jacobi, ay_jacobi, label="Jacobi's Method")
plt.plot(ax_gauss, ay_gauss, label="Gauss-Saidel's Method")
plt.legend(loc="upper right")
plt.ylabel('log||x(n) - x(*)||')
plt.xlabel('n')

plt.show()
