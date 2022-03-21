# 4. Mamy trzy liczby całkowite, x, y, z reprezentujące wymiary prostopadłościanu,
# oraz pewną liczbę naturalną n. Wypisz listę wszystkich możliwych współrzędnych (i, j, k)
# na trójwymiarowej siatce, gdzie i+j+k nie jest równe n.
# Warunki: 0 ≤ i ≤ x, 0 ≤ j ≤ y, 0 ≤ k ≤ z.
# Rozwiązanie zapisz w postaci list składanych (list comprehesion),
# ale można zacząć od zagnieżdżonych pętli. Przykład. Niech x = 1, y = 1, z = 2, n = 3.
# Lista wszystkich permutacji trójek [i, j, k] w tym przykładzie:
# [[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [0,1,2], [1,0,0],[1,0,1], [1,0,2], [1,1,0], [1,1,1], [1,1,2]].
# Elementy, które nie sumują się do 3 to:
# [[0,0,0], [0,0,1], [0,0,2], [0,1,0],[0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,2]].
# Parametry x,y,z,n wczytać na początku za pomocą funkcji input().

x = int(input("[Liczba całkowita] x = "))
y = int(input("[Liczba całkowita] y = "))
z = int(input("[Liczba całkowita] z = "))
n = int(input("[Liczba naturalna] n = "))
l = list()

for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            l.extend([[i, j, k]])
            newl = [a for a in l if (a[0]+a[1]+a[2] != n)]

print(l)
print(newl)
