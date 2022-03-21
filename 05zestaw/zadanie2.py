from math import hypot, atan, sin, cos


class Zespolona:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def conjugate(self):
        return self.__class__(self.r, -self.i)

    def argz(self):
        return atan(self.i / self.r)

    def __abs__(self):
        # (sqrt(x^2+y^2))
        return (self.r**2+self.i**2)**(-1/2)

    def __repr__(self):
        return f"Zespolona({str(self.r)}, {str(self.i)})"

    def __str__(self):
        if self.i < 0:
            return str(self.r) + str(self.i) + "i"
        else:
            return str(self.r) + "+" + str(self.i) + "i"

    def __add__(self, other):
        if not isinstance(other, Zespolona):
            return Zespolona(self.r + other, self.i)
        return Zespolona(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return Zespolona(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        if not isinstance(other, Zespolona):
            return Zespolona(self.r * other, self.i*other)
        return Zespolona(self.r*other.r - self.i*other.i, self.r*other.i + other.r*self.i)

    def __radd__(self, other):
        return Zespolona(self.r + other, self.i)

    def __rmul__(self, other):
        return Zespolona(self.r * other, self.i*other)

    def __rsub__(self, other):
        return Zespolona(other - self.r, - self.i)

    def __eq__(self, other):
        return (self.r == other.r and self.i == other.i)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __pow__(self, other):
        tmp = Zespolona(cos(other*self.argz()), sin(other*self.argz()))
        #a = (self * (self.conjugate()))**(other/2)
        a = (self.r**2+self.i**2)**(other/2)
        return a*tmp


def main():
    print("Liczby zespolone")
    a = Zespolona(2, 5)
    b = Zespolona(1, -3)
    print(a)
    print(b)
    b_copy = eval(repr(b))
    print(type(b_copy), b_copy.r, b_copy.i)
    print(a + b)
    print(a - b)
    print(a + 4)
    print(7 - a)
    print(a * 4)
    print(a * (-4))
    print(a == Zespolona(2, 5))
    print(a == b)
    print(a != b)
    print(a != Zespolona(2, 5))
    print(a ** 2)
    print(b ** 4)


if __name__ == "__main__":
    main()


# Liczby zespolone
# (2+5j)
# (1-3j)
# <class '__main__.Zespolona'> 1 -3
# (3+2j)
# (1+8j)
# (6+5j)
# (5-5j)
# (8+20j)
# (-8-20j)
# True
# False
# True
# False
# (-21+20j)
# (28+96j)
