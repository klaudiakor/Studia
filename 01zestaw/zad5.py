# 5. Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string,
# a potem go wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# [ZADANIE 3.6]


width = input("Prosze podac szerokosc prostokata: ")
height = input("Prosze podac wysokosc prostokata: ")

rectangle = ""
first_line = "+"
second_line = "|"


for i in range(0, int(width)):
    first_line += "---+"
    second_line += "   |"


for j in range(0, int(height)):
    rectangle += first_line
    rectangle += '\n'
    rectangle += second_line
    rectangle += '\n'
rectangle += first_line


print(rectangle)
