def policz(pudelko):
    for liczba in pudelko:
        if liczba % 2 == 0:
            return liczba
    return None
moje_liczby = [1, 21, 3, 4, 5]
print(policz(moje_liczby))



