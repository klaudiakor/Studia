import numpy as np
import time

start_time = time.time()
N = 50
z = np.zeros(N)
q = np.zeros(N)
w = np.zeros(N)


def mxA(row, column):
    if row == column:
        return 9
    elif row + 1 == column:
        return 7
    else:
        return 0


def vec_b():
    return 5


def vec_u():
    return 1


def sum(j):
    # sum = u(i,i+1)x(i+1)+0
    return mxA(j-1, j)


def count_vec_z():
    # Az = b
    z[N-1] = vec_b()/mxA(N-1, N-1)
    for i in range(N-1, 0, -1):
        z[i-1] = (vec_b()-(sum(i)*z[i]))/mxA(i, i)


def count_vec_q():
    # Aq = u
    q[N-1] = vec_u()/mxA(N-1, N-1)
    for i in range(N-1, 0, -1):
        q[i-1] = (vec_u()-(sum(i)*q[i]))/mxA(i, i)


def count_vec_w():
    # w = z - (v^T * z)/(1 + v^T * q) * q
    vTz, vTq = 0, 0
    for i in range(0, N):
        vTz += z[i]
        vTq += q[i]

    frac = vTz/(1+vTq)

    for j in range(0, N):
        w[j] = z[j]-q[j]*frac


count_vec_z()
# print(z)
count_vec_q()
# print(q)
count_vec_w()
print("wektor rozwiązań:")
print(w)

print("--- %s seconds ---" % (time.time() - start_time))


def latex():
    res = r"\begin{pmatrix}"
    for _ in range(0, 25):
        res += str(w[_])
        if _ != N-1:
            res += r"\\"
    res += r"\end{pmatrix}"
    res2 = r"\begin{pmatrix}"
    for _ in range(25, N):
        res2 += str(w[_])
        if _ != N-1:
            res2 += r"\\"
    res2 += r"\end{pmatrix}"
    print(res+res2)


# latex()
