from multipledispatch import dispatch


class Figura(object):
    def __init__(self):
        print("Figura init")


class Prostokat(Figura):
    # zdefiniuj __init__ i argumenty x, y
    def __init__(self, x, y):
        print("Prostokat init")
        self.x = x
        self.y = y


class Kwadrat(Prostokat):
    # __init__ i jeden argument x, wołanie __init__ bazowego
    def __init__(self, x):
        super().__init__(x, x)
        print("Kwadrat init")


@dispatch(Figura)
def pole(instance: Figura):
    print("Pole: Figura")
    return 0


@dispatch(Prostokat)
# zdefiniuj pole, zwróć x*y z instancji
def pole(instance: Prostokat):
    return instance.x * instance.y


@dispatch(Prostokat, int, int)
# funkcja pole, najpierw przypisz argumenty do x, y instancji, potem policz pole powierzchni
def pole(instance: Prostokat, x: int, y: int):
    instance.x = x
    instance.y = y
    return pole(instance)


@dispatch(Kwadrat)
# funkcja pole
def pole(instance: Kwadrat):
    return instance.x * instance.x


@dispatch(Kwadrat, int)
# funkcja pole z podanym argumentem boku
def pole(instance: Kwadrat, x: int):
    instance.x = x
    return pole(instance)


# testy
a, b, c = Figura(), Prostokat(2, 4), Kwadrat(2)

bb = pole(b, 5, 6)
print(bb)
cc = pole(c, 7)
print(cc)


def polaPowierzchni(listaFigur):
    for i in listaFigur:
        print(pole(i))  # polymorphism at runtime


polaPowierzchni([a, b, c])
