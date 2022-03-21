# 2. Mamy daną listę sekwencji(listy lub krotki) różnej długości zawierających liczby. Znaleźć listę
# zawierającą sumy liczb z tych sekwencji. Przykładowa sekwencja[[], [4], (1, 2), [3, 4], (5, 6, 7)],
# spodziewany wynik[0, 4, 3, 7, 18]. [ZADANIE 3.9]

sekwencja = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
l = list()
for item in sekwencja:
    result = 0
    for i in item:
        result += i
    l.append(result)

print(l)
