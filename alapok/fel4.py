# Importálások
import time
import random


# Első feladat
def first_task():
    print("Kérlek add meg a neved!\n")
    first_name = str(input("Vezetéknév: "))
    last_name = str(input("Keresztnév: "))

    teljes_nev = (first_name + " " + last_name)

    print(f"\nÜdvözöllek {teljes_nev}!")


# Második feladat
def second_task():
    your_num = int(input("Kérlek adj meg egy számot! "))
    if your_num <= 10:
        lucky_num = your_num + random.randint(1, 9) / 2 + 3
        print(f"A te szerencseszámod:\n{int(lucky_num)}")
    else:
        print("Kérlek adj meg egy számot 1 és 10 között")
        second_task()


time.sleep(1)
print("\n-------------------------")
print("Első feladat")
print("-------------------------\n")
first_task()
time.sleep(1)
print("\n-------------------------")
print("Második feladat")
print("-------------------------\n")
second_task()
