# 1. Mamy zagnieżdżoną listę, na przykład:
# list1 = [1, 2, [3, 4, [5, 6], 5], 3, 4].
# Dodaj element o kolejnej wartości w najbardziej zagnieżdżonej liście.
# W tym przypadku 7 w miejscu [1, 2, [3, 4, [5, 6, 7], 5], 3, 4].
# Napisz program, który zrobi to uniwersalnie, dla dowolnego zagnieżdżenia,
# np. dla [1 [2, 3] 4] chodzi o
# [1 [2, 3, 4] 4], dla [3, 4,[2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]
# powinno być [3, 4, [2, [1, 2, [7, 8, 9], 3, 4], 3, 4], 5, 6, 7].

list1 = [1, 2, [3, 4, [5, 6], 5], 3, 4]
list2 = [1, [2, 3], 4]
list3 = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]


def fun(list):
    list_str = str(list)
    for i in list_str:
        spot_to_split = list_str.index(']')
        break
    next_value = int(list_str[spot_to_split-1])+1
    result = list_str[:spot_to_split] + ', ' + \
        str(next_value) + list_str[spot_to_split:]
    print(result)


fun(list1)
fun(list2)
fun(list3)
