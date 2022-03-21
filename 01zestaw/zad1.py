# 1. Narysować odwróconą piramidę z gwiazdek o zadanej (zapytać przez input) długości nieparzystej, np.
# dla 9, tak żeby co kolejny wiersz malało o dwie gwiazdki:
# *********
#  *******
#   *****
#    ***
#     *

def triangle(height):
    for i in range(0, height):
        print(' ' * i + '*' * (height-2*i))


print('Prosze podac nieparzysta liczbe, ktora bedzie wysokoscia piramidy: ')
triangle_height = input()

# spr czy podana liczb jest nieparzysta
if int(triangle_height) % 2 == 0:
    print('Liczba musi byc nieparzysta!\n')
else:
    triangle(int(triangle_height))
