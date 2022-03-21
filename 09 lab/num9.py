import numpy as np
import matplotlib.pyplot as plt

true_value = np.arcsin(0.37)

# funkcje i ich pochodne


def f(x):
    return np.sin(x) - 0.37


def df(x):
    return np.cos(x)


def g(x):
    return (np.sin(x) - 0.37)**2


def dg(x):
    return 2*(np.sin(x)-0.37)*np.cos(x)


def u(x):
    return (1/2)*(np.sin(x)-0.37)*(1/np.cos(x))


def du(x):
    return (1/2)*((np.sin(x)-0.37)*np.tan(x)*(1/np.cos(x))+1)


def Bisection(f, a, b, eps=0.1e-6, maxiter=100):
    xi_points = np.array([], float)
    print("> Metoda bisekcji")
    error = abs(b-a)
    for iteration in range(maxiter):
        if error > eps:
            x = (b+a)/2
            if f(a)*f(b) >= 0:
                print("Error: takie same znaki na krańcach przedziału")
                break
            elif f(x)*f(a) < 0:
                b = x
                error = abs(b-a)
            elif f(x) * f(b) < 0:
                a = x
                error = abs(b-a)
            else:
                print("Coś poszło nie tak")
                break
        else:
            break

        xi_points = np.append(xi_points, abs(true_value - (a+b)/2))

    print("Ilość iteracji: ", iteration)
    print((a+b)/2)
    return xi_points


def Falsi(f, a, b, eps=1.0e-6, maxfpos=100):
    print("> Metoda falsi")
    xi_points = np.array([], float)
    x = 0
    i = 0
    if f(a)*f(b) < 0:
        for iteration in range(1, maxfpos+1):
            x = b-(b-a)/(f(b)-f(a))*f(b)
            if abs(f(x)) < eps:
                break
            elif f(a)*f(b) < 0:
                b = x
            else:
                a = x
            xi_points = np.append(xi_points, abs(true_value - x))
    else:
        print("W zadanym przedziale nie istnieje pierwiastek")
    print("Ilość iteracji: ", iteration)
    print(x)
    return xi_points


def Secant(f, a, b, eps=1.0e-6, maxiter=100):
    xi_points = np.array([], float)
    print("> Metoda siecznych")
    for iteration in range(maxiter):
        x = b-(b-a)/(f(b)-f(a))*f(b)
        if abs(x-b) < eps:
            break
        else:
            a = b
            b = x
        xi_points = np.append(xi_points, abs(true_value-x))
    else:
        print("Osiągnięto maksymalną ilość iteracji!")
    print("Ilość iteracji: ", iteration)
    print(x)
    return xi_points


def Newton(f, x, df, eps=1.0e-6, maxiter=100):
    xi_points = np.array([], float)
    print("> Metoda Newtona")
    for iteration in range(maxiter):
        xnew = x-f(x)/df(x)
        if abs(xnew - x) < eps:
            break
        x = xnew
        xi_points = np.append(xi_points, abs(true_value - xnew))
    print("Ilość iteracji: ", iteration)
    print(xnew)
    return xi_points

# wyniki


print("--- funkcja (a) ---")
bf = Bisection(f, 0, np.pi/2)
ff = Falsi(f, 0, np.pi/2)
sf = Secant(f, 0, np.pi/2)
nf = Newton(f, 0, df)

print()

print("--- funkcja (b) ---")
sg = Secant(g, 0, 1, eps=1.0e-8)
ng = Newton(g, 0, dg, eps=1.0e-8)

print()

print("--- ulepszenie dla funkcji b) ---")
su = Secant(u, 0, 1, eps=1.0e-8)
nu = Newton(u, 0, du, eps=1.0e-8)

print()

print("Poprawny wynik: ", true_value)


# wykresy

plt.title("Porównanie metod szukania miejsca zerowego\nfunkcji f(x)")
plt.yscale('log')
plt.xlabel('numer iteracji')
plt.ylabel('|x* - xi|')
plt.plot(np.linspace(0, len(bf), len(bf)), bf, '-o', label="bisekcja")
plt.plot(np.linspace(0, len(ff), len(ff)), ff, '-o', label="metoda falsi")
plt.plot(np.linspace(0, len(sf), len(sf)), sf, '-o', label="metoda siecznych")
plt.plot(np.linspace(0, len(nf), len(nf)), nf, '-o', label="metoda Newtona")
plt.legend()
plt.show()

plt.title("Porównanie metod szukania miejsca zerowego\nfunkcji g(x)")
plt.yscale('log')
plt.xlabel('numer iteracji')
plt.ylabel('|x* - xi|')
plt.plot(np.linspace(0, len(sg), len(sg)), sg, '-o', label="metoda siecznych")
plt.plot(np.linspace(0, len(ng), len(ng)), ng, '-o', label="metoda Newtona")
plt.legend()
plt.show()

plt.title("Porównanie metod szukania miejsca zerowego\nfunkcji u(x) = g(x)/g'(x)")
plt.yscale('log')
plt.xlabel('numer iteracji')
plt.ylabel('|x* - xi|')
plt.plot(np.linspace(0, len(su), len(su)), su, '-o', label="metoda siecznych")
plt.plot(np.linspace(0, len(nu), len(nu)), nu, '-o', label="metoda Newtona")
plt.legend()
plt.show()
