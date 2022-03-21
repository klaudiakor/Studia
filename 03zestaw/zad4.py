# 4. Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left
# do right włącznie. Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną
# i rekurencyjną. [ ZADANIE 4.5 ]

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
L2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def iteration_replace(L, left, right):
    if(right-left) == 1:
        L[left], L[right] = L[right], L[left]
    else:
        stop = (right-left)//2
        if (right-left) % 2 == 1:
            stop += 1
        for i in range(stop):
            L[left], L[right] = L[right], L[left]
            left += 1
            right -= 1


def recursion_replace(L, left, right):
    L[left], L[right] = L[right], L[left]
    left += 1
    right -= 1
    if left < right:
        return recursion_replace(L, left, right)


print(L)
iteration_replace(L, 2, 7)
print(L)
recursion_replace(L2, 2, 7)
print(L2)
