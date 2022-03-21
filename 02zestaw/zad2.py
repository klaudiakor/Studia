# 2. Napisz funkcję, która sprawdzi, czy podany (jako parametr wejściowy – funkcja input) rok,
# z zakresu 1900 – 100000, jest rokiem przestępnym. Za taki rok uważa się rok,
# który jest podzielny przez 4, ale jeśli jest podzielny przez 100, to nie jest to rok przestępny,
# chyba że jest dodatkowo podzielny przez 400 – to jest to rok przestępny.
# Np. 1900 to nie jest rok przestępny, ale 2000 jest. Proszę zwracać True / False.


def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return False


x = input("Rok: ")
if int(x) < 1900 or int(x) > 100000:
    print("Prosze podac rok z zakresu 1900 – 100000")
if is_leap(int(x)):
    print(x + " jest rokiem przestępnym")
else:
    print(x + " nie jest rokiem przestępnym")
