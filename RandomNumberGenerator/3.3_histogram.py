# Klaudia Korczak
# napisac generator liczb pseudolosowych generujacy liczby o funkcji gestosci prawdopodobienstwa
# bedacej bokami trapezu o wierzcholkach w punktach (-1,0), (0,1/3),(2,1/3),(3,0).
# Korzystajac z wylosowanych liczb prosze narysowac unormowany histogram oddajacy ”eksperymentalna”
# funkcje gestosci prawdopodobienstwa i porownac ja z teoretyczna.
# Wykonac to porownanie dla roznej liczby (np. 10^3, 10^5) losowanych liczb.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed()


def trapez(x):
    if(x >= -1 and x < 0):
        return 1/3*x + (1/3)
    elif(x >= 0 and x < 2):
        return 1/3
    elif(x >= 2 and x <= 3):
        return ((-1)/3)*x + 1
    else:
        print("[Error]: x poza zakresem")


def obrucona_dystrybuanta(y):
    if (y >= 0 and y < 1/6):
        return np.sqrt(6*y) - 1
    elif (y >= 1/6 and y < 5/6):
        return (3*y) - (1/2)
    elif (y >= 5/6 and y < 1):
        return 3 - np.sqrt(((-6)*y)+6)
    else:
        print("[Error]: y poza zasięgiem")


def wyniki(x):
    results = list()
    for i in range(0, x+1):
        results.append(obrucona_dystrybuanta(np.random.random()))
    return results


def wykres_teoretyczny():
    x = np.arange(-1, 3.1, 0.1)
    y = list()
    for i in x:
        y.append(trapez(i))
    plt.plot(x, y, label="Funkcja matematyczna", color='orange')


def wykres_eksperymentu(ilosc_losowan):
    wyniki(int(ilosc_losowan))
    plt.title(str(ilosc_losowan) + " liczb w eksperymencie")
    plt.hist(wyniki(ilosc_losowan), bins=50, density=True, color='lightblue',
             edgecolor='darkblue', label="Funkcja eksperymentalna")


def rysowanie_wykresow(ilosc_losowan):
    wykres_teoretyczny()
    wykres_eksperymentu(ilosc_losowan)
    plt.legend(loc="lower center")
    plt.show()


rysowanie_wykresow(1000)
rysowanie_wykresow(100000)
rysowanie_wykresow(1000000)
