import numpy as np
import time

start_time = time.time()

N = 1000


def mxA(row, column):
    if row == column:
        return 10
    elif row + 1 == column:
        return 8
    else:
        return 1


mx_str = ''
for i in range(N):
    for j in range(N):
        mx_str += str(mxA(i, j)) + ' '
    if not i == N-1:
        mx_str += ';'

mx = np.matrix(mx_str)
# print(mx)

b = np.full((N, 1), 5)
# print(b)

y = np.linalg.solve(mx, b)
# print(y)

print("--- %s seconds ---" % (time.time() - start_time))
