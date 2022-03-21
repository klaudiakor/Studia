# singledispatch oraz singledispatchmethod

from functools import singledispatch, singledispatchmethod


@singledispatch
def fun(arg):
    print("Default fun", arg)


@fun.register
def _(arg: int):
    print("arg is an int", arg)


@fun.register
def _(arg: list):
    print("arg is an int", arg)
    for item in arg:
        print(item)


class A:
    @singledispatchmethod
    def foo(self, arg):
        print("default")

    @foo.register
    def _(self, arg: int):
        print("arg is int")

    @foo.register
    def _(self, arg: bool):
        print("arg is bool")


def main():
    fun(1)
    fun("a")
    fun([1, 2, 3])
    a = A()
    a.foo(5)
    a.foo(False)


main()
