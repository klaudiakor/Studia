import numpy as np

A1 = np.matrix([[2.40827208, -0.36066254, 0.80575445, 0.46309511, 1.20708553],
                [-0.36066254, 1.14839502, 0.02576113, 0.02672584, -1.03949556],
                [0.80575445, 0.02576113, 2.45964907, 0.13824088, 0.0472749],
                [0.46309511, 0.02672584, 0.13824088, 2.05614464, -0.9434493],
                [1.20708553, -1.03949556, 0.0472749, -0.9434493, 1.92753926]])
A2 = np.matrix([[2.61370745, -0.6334453, 0.76061329, 0.24938964, 0.82783473],
                [-0.6334453, 1.51060349, 0.08570081, 0.31048984, -0.53591589],
                [0.76061329, 0.08570081, 2.46956812, 0.18519926, 0.13060923],
                [0.24938964, 0.31048984, 0.18519926, 2.27845311, -0.54893124],
                [0.82783473, -0.53591589, 0.13060923, -0.54893124, 2.6276678]])

b = np.matrix([[5.40780228], [3.67008677],
               [3.12306266], [-1.11187948], [0.54437218]])
c = np.matrix([[10**(-5)], [0], [0], [0], [0]])
b_ = b + c

y1 = np.linalg.solve(A1, b)
y1_ = np.linalg.solve(A1, b_)
y2 = np.linalg.solve(A2, b)
y2_ = np.linalg.solve(A2, b_)

print("y1 =\n" + str(y1) + "\n\ny1' =\n" + str(y1_) +
      "\n\ny2 =\n" + str(y2) + "\n\ny2' =\n" + str(y2_) + '\n')

x1 = y1 - y1_
x2 = y2 - y2_

print("delta 1: " + str(np.linalg.norm(x1)))
print("delta 2: " + str(np.linalg.norm(x2)))


# obliczenie wartości własnych macierzy
# print("max wartość własna A1: ")
# print(np.max(np.linalg.eigvals(A1)))
# print("min wartość własna A1: ")
# print(np.min(np.linalg.eigvals(A1)))
# print("kappa 1:")
# print(np.max(np.linalg.eigvals(A1))/np.min(np.linalg.eigvals(A1)))

# print("max wartość własna A2: ")
# print(np.max(np.linalg.eigvals(A2)))
# print("min wartość własna A2: ")
# print(np.min(np.linalg.eigvals(A2)))
# print("kappa 2:")
# print(np.max(np.linalg.eigvals(A2))/np.min(np.linalg.eigvals(A2)))
