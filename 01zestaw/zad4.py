# 4. Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające
# się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). Należy zbudować
# pełny string, a potem go wypisać. [ZADANIE 3.5]
# |....|....|....|....|....|....|....|....|....|....|....|....|
# 0    1    2    3    4    5    6    7    8    9   10   11   12


def space_num(x):
    return 5-len(x)


x = input("Prosze podac dlugosc miarki: ")
x_num = int(x)

for i in range(0, x_num):
    print("|....", end='')
print("|")
print("0", end='')
for i in range(1, x_num+1):
    print(' '*space_num(str(i)) + str(i), end='')
