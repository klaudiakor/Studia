# 3. Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na
# liczby arabskie (podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący
# całą liczbę [funkcja roman2int()]. [ ZADANIE 3.10 ]

liczby = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
# inne metody:
# liczby = dict([("I", 1), ("V", 5), ("X", 10), ("L", 50),
# ("C", 100), ("D", 500), ("M", 1000)])
# liczby = dict(zip(["I", "V", "X", "L", "C", "D", "M"],
#               [1, 5, 10, 50, 100, 500, 1000]))

rzymska = ""

while True:
    rzymska = input("Podaj cyfre rzymska: ").upper()
    if rzymska == "STOP":
        break

    L = list(rzymska)
    result = 0
    n = len(rzymska)

    for index, value in enumerate(L):
        if index < n-1 and liczby[value] < liczby[rzymska[index+1]]:
            result -= liczby[value]
        else:
            result += liczby[value]
    print(result)
