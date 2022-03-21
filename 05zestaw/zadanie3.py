# podpunkt A)
# zdefiniować w ramach klasy A:
#   - funkcję foo(self, x),
#   - metodę klasy class_foo,
#   - metodę statyczną static_foo,
# tak, żeby kod poniżej drukował treści jak w komentarzach

from abc import ABC, abstractmethod


class A(object):
    def foo(self, x):
        print("foo "+str(x))

    @classmethod
    def class_foo(self, x):
        print("class_foo " + str(x))

    @staticmethod
    def static_foo(x):
        print("static_foo " + str(x))


a = A()
a.foo(123)  # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
A.foo(a, 123)  # ditto
a.class_foo(123)  # class_foo(<class '__main__.A'>, 123)
A.class_foo(123)  # ditto
a.static_foo(123)  # wykonanie static_foo(123)
A.static_foo(123)  # ditto

# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu


class Baza(ABC):
    @abstractmethod
    def abs_foo(self):
        pass


class Potomek1(Baza):
    def abs_foo(self):
        print("Potomek 1 wykonuje abs_foo")


class Potomek2(Baza):
    def abs_foo(self):
        print("Potomek 2 wykonuje abs_foo")


p1 = Potomek1()
p1.abs_foo()
p2 = Potomek2()
p2.abs_foo()


# podpunkt C)
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu

class Person(object):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


Ala = Person("Ala")
print(Ala.name)
Ala.name = "Adam"
print(Ala.name)
