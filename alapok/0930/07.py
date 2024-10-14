import random


def coinflip():
    result = random.choice(["Fej", "Írás"])
    choice = str(input("Kérlek válassz fej vagy írás? (F/I) "))
    print(f"A te választásod: {choice}\nAz eredmény pedig: {result}")


coinflip()