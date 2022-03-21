# 3. Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x
# oraz trzecią potęgę x. Zatrzymanie programu następuje po wpisaniu z klawiatury stop. Jeżeli
# użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować
# pracę. [ZADANIE 3.4]

def input_is_a_number(input):
    try:
        value = float(input)
    except ValueError:
        print("[Error] Nie podano liczby")
        return False
    return True


while True:
    x = input("Prosze podac liczbe rzeczywista: ")
    if x == "stop":
        break
    if not input_is_a_number(x):
        continue
    x_pow = float(x)**3
    print("x = " + x)
    print("x^3 = " + str(x_pow))
