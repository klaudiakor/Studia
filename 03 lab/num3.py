import numpy as np
N = 100

vec = np.empty(N)
for i in range(N):
    vec[i] = i+1

diagonal = np.empty(N)
diagonal.fill(1.2)

under_diagonal = np.empty(N)
under_diagonal.fill(0.2)
under_diagonal[0] = 0

over_diagonal = np.empty(N-1)
for i in range(1, N):
    over_diagonal[i-1] = 0.1/i

two_over_diagonal = np.empty(N-2)
for i in range(1, N-1):
    two_over_diagonal[i-1] = 0.4/(i*i)


def LU():

    for i in range(1, N):

        if i == N-1:
            under_diagonal[i] = under_diagonal[i] / diagonal[i - 1]
            diagonal[i] = diagonal[i] - \
                (under_diagonal[i] * over_diagonal[i - 1])
        elif i == N-2:
            under_diagonal[i] = under_diagonal[i] / diagonal[i - 1]
            diagonal[i] = diagonal[i] - \
                (under_diagonal[i] * over_diagonal[i - 1])
            over_diagonal[i] = over_diagonal[i] - \
                (under_diagonal[i] * two_over_diagonal[i - 1])

        else:
            under_diagonal[i] = under_diagonal[i] / diagonal[i - 1]
            diagonal[i] = diagonal[i] - \
                (under_diagonal[i] * over_diagonal[i - 1])
            over_diagonal[i] = over_diagonal[i] - \
                (under_diagonal[i] * two_over_diagonal[i - 1])
            two_over_diagonal[i] = two_over_diagonal[i]


def forward_sub(x):

    y = np.zeros(N)
    for i in range(0, N):
        if i == 0:
            y[i] = x[i]
        else:
            y[i] = x[i] - under_diagonal[i] * y[i - 1]

    return y


def backward_sub(y):

    x = np.zeros(N)
    for i in range(N-1, -1, -1):
        if i < N-2:
            x[i] = (y[i] - ((two_over_diagonal[i] * x[i + 2]) +
                    (over_diagonal[i] * x[i + 1]))) / diagonal[i]
        elif i == N-2:
            x[i] = (y[i] - (over_diagonal[i] * x[i + 1])) / diagonal[i]
        else:
            x[i] = y[i] / diagonal[i]

    return x


def det(x):
    det = 1.0
    for i in x:
        det *= i

    return det


LU()
detA = det(diagonal)

z = forward_sub(vec)
y = backward_sub(z)

print("Wektor rozwiązań: ")
print(y)

print("\ndet(A) = ", detA)
