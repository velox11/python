print("Podaj wiek")
wiek = int(input())
print(f"Twoj wiek to {wiek}")
roznica = 18 - wiek
if roznica <= 0:
    print("jestes pelnoletni")
else:
    print(f"Za {roznica} bedziesz pelnoletni")
