print("WITAJ Kolego")
A = float(input("Podaj mi liczba A "))
B = float(input("Podaj mi liczbe B "))
X = input('Podaj mi dzialanie *, /, +, -')

if X == "*":
        wynik = A * B
        print (f'Twoj wynik wynoski: {wynik}')
elif X == "/":
          wynik = A / B
          print(f'Twoj wynik wynosi: {wynik}')
elif X == "+":
          wynik = A + B
          print(f'Twoj wynik wynosi: {wynik}')
elif X == "/":
          wynik = A - B
          print(f'Twoj wynik wynosi: {wynik}')
else:
          print('Error')

