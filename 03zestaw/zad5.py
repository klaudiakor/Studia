# 5. W ramach zapoznania się z klasami, proszę napisać klasę o nazwie Bug taką, żeby zawierała licznik
# wskazujący aktualną liczbę powołanych do życia obiektów, identyfikator (lokalną zmienną obiektu, do
# której przypiszemy aktualny powiększony licznik). Licznik powinien rosnąć wraz z wywołaniem __init__
# oraz maleć z wywołaniem __del__ (uwaga: współdzielony licznik będziemy używać w zapisie
# Bug.licznik). Proszę też zdefiniować __str__ wypisującą licznik i bieżące id. Finalnie, niech dla kodu:
# bugs = []
# for i in range(100):
#  bugs.append(Bug())
#  print(bugs[-1])
# wypisują się licznik, identyfikator, a przy niszczeniu obiektu w __del__ niech będzie też print informacji typu
# ‘Koniec’, licznik, identyfikator


class Bug():
    licznik = 0  # licznik wskazujący aktualną liczbę powołanych do życia obiektów

    def __init__(self):
        Bug.licznik += 1
        self.identyfikator = Bug.licznik  # +1?

    def __del__(self):
        Bug.licznik -= 1
        print("Koniec", "licznik: ", str(Bug.licznik),
              "id: ", str(self.identyfikator))

    def __str__(self):  # wypisuje licznik i bieżące id
        result = "licznik: " + str(Bug.licznik) + \
            " id: " + str(self.identyfikator)
        return result


bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])
