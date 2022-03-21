# CIĄG FIBONACCIEGO
# Proszę napisać (uzupełnić poniższy szkielet) kod tak, żeby właśnie powstawał słownik
# – pamięć podręczna z poprzednimi wyliczonymi wartościami
# i z nich korzystać, a wyliczać nowe tylko gdy jeszcze nie były policzone wcześniej.
# Słownik proszę zrobić w dekoratorze.

import functools


def pamiec(func):
    memory = {}

    @functools.wraps(func)
    def wrapper(x):
        if x not in memory:
            memory[x] = func(x)
        return memory[x]
    return wrapper


@pamiec
def fibonacci(n):
    return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


for i in range(100):
    print(fibonacci(i))



