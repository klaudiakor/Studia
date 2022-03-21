# 5. Mamy liczbę naturalną N w zapisie binarnym (czyli składa się tylko z 0 i 1).
# Binarna przerwa to sekwencja zer otoczonych z lewej i prawej strony 1.
# Na przykład liczba 9 (decymalnie) binarnie wynosi 1001 i posiada jedną binarną przerwę długości 2.
# Liczba 529 ma binarną reprezentację 1000010001, zatem ma dwie binarne przerwy,
# o długości 4 i 3. Liczba 20 ma reprezentację 10100 zawiera zatem jedną binarną przerwę
# o długości 1. Liczba 15 ma reprezentację 1111, a zatem żadnej binarnej przerwy.
# Napisz funkcję: def fun(N)
# która dla podanej liczby naturalnej N (uwaga: liczby w systemie dziesiętnym)
# zwraca długość jej najdłuższej binarnej przerwy, albo 0, jeśli nie ma ani jednej przerwy.
# Na przykład, dla N = 1041, które binarnie jest 10000010001, ma najdłuższą przerwę binarną 5.
# Należy przyjąć, że argument N może być z przedziału [1..2147483647].
# Wskazówka: warto skorzystać z operatora przesunięcia bitowego >>
# Generalnie można podejrzeć jak wygląda liczba w zapisie binarnym poprzez rzutowanie bin(N).

def fun(N):
    meet_one = False
    counter = 0
    a = []
    while N:
        # print(bin(N))
        if meet_one and N & 1 == 0:
            # N -> 0
            counter += 1

        if N & 1:
            # N -> 1
            meet_one = True
            a.append(counter)
            counter = 0
        N = N >> 1

    return max(a)


N = int(input("[liczba dziesiętna] N = "))
if N < 1 or N > 2147483647:
    print("Prosze podac liczbe z przedzialu [1..2147483647]")
print(fun(N))
