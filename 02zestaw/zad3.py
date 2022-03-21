# 3. Dla dowolnego podanego łańcucha znakowego wypisać:
# - ile jest w nim słów (poprzez słowo rozumiemy ciąg co najmniej jednego znaku
# innego niż znak przestankowy, https://pl.wikipedia.org/wiki/Interpunkcja),
# ile liter, oraz wypisać statystykę częstości występowania poszczególnych liter.

text = input("Łańcuch znakowy: ")
word_list = text.split()

words_num = len(word_list)
print("Ilość słów: " + str(words_num))


def count(letter, text):
    text.count(letter)


alphabet = "a;b;c;d;e;f;g;h;i;j;k;l;m;n;o;p;r;s;t;u;v;w;x;y;z"
alphabet_list = alphabet.split(";")

letter_num = 0

for _ in alphabet_list:
    result = text.count(_)
    if result != 0:
        letter_num += result
        print("Ilość wystąpień " + _ + ": " + str(result))


print("Ilość liter: " + str(letter_num))
