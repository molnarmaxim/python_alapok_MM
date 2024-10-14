number = int(input("Kérlek adj meg egy számot! "))

if number % 3 == 0 and number % 4 == 0:
    print("A szám osztható 3-mal és 4-gyel is.")
elif number % 3 != 0 and number % 4 == 0:
    print("A szám csak 4-gyel osztható.")
elif number % 3 == 0 and number % 4 != 0:
    print("A szám csak 3-mal osztható.")
elif number % 3 != 0 and number % 4 != 0:
    print("A szám se hárommal se néggyel nem osztható!")
else:
    print("500 internal server error")