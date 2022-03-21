# 2. Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3. [ ZADANIE 3.3]


for i in range(0, 31):
    if i % 3 != 0:
        print(i, end=" ")
