import random

randomnumber = random.randint(1, 3)
yournumber = int(input("Kérlek adj meg egy számot 1 és 3 között! "))


def task():
    if 3 >= yournumber >= 0:
        print(f"A te számod: {yournumber}\nA gép száma: {randomnumber}")
    else:
        print("Hiba történt! Az általad megadott szám nem 1 és 3 között van.")


task()