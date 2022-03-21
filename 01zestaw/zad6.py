# 6. Dla dwóch sekwencji znaleźć: (a) listę elementów występujących jednocześnie w obu sekwencjach
# (bez powtórzeń), (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń). P.s. można
# doczytać sobie o typie set [ZADANIE 3.8]

list1 = ['jabłko', 'mango', 'marchew', 'kiwi']
list2 = ['ananas', 'jabłko', 'marchew', 'banan']

set1 = set(list1)
set2 = set(list2)

print(list1, list2)
print(set1.intersection(set2))  # (A)
print(set1.union(set2))  # (B)
