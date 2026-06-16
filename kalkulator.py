print("Witaj w Kalkulatorze")
A = int(input('Podaj liczba A '))
B = int(input('Podaj liczbe B '))
x = input('Podaj dzialanie mozliwe + lub -')

if x == "+": 
    wynik = A + B
    print(f'wynik dodawnia wynosi {wynik}')
#    print(wynik)
elif x == "-":
    wynik = A - B
    print(f'wynik odejmowanai wynosi  {wynik}')
#    print(wynik)
else:
    print('error')
    


