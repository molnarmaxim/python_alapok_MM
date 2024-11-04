"""0. Feladat: Számok kiírása
Írj egy programot, amely kiírja az 1-től 20-ig a számokat!
1
2
3
...
"""

import time

def first_task():
    for x in range(1, 21):
        print(x)
        x += 1

first_task()
print("\n")
time.sleep(1)

"""
0.b Feladat: Számok kiírása
Írj egy programot, amely kiírja az 1-től 20-ig a számokat a minta alapján!
1 2 3 4 ...
"""

def second_task():
    for x in range(1, 21):
        print(x, end=" ")
        x += 1

second_task()
time.sleep(1)

"""
1. Feladat: Páros számok kiírása
Írj egy programot, amely kiírja az 1 és 20 közötti páros számokat!
2
4
6
"""
print("\n")
def third_task():
    for x in range(1, 21):
        if x % 2 == 0:
            print(x)

third_task()
time.sleep(1)
print("\n")


"""
2. Feladat: Számok összege
Készíts egy programot, amely kiszámítja és kiírja az 1 és 10 közötti számok
összegét!
Az összeg: __
"""

def fourth_task():
    osszeg = 0
    for x in range(1, 10):
        osszeg += x
    print(f"Összeg: {osszeg}")

fourth_task()
time.sleep(1)
print("\n")

"""
2.b Feladat: Számok összege
Készíts egy programot, amely kiszámítja és kiírja az 1 és 100 közötti számok
összegét!
Az összeg: __
"""

def fifth_task():
    osszeg = 0
    for x in range(1, 101):
        osszeg += x
    print(f"Összeg: {osszeg}")

fifth_task()
time.sleep(1)
print('\n')

"""3. Feladat: Szorzótábla
Készíts egy programot, amely kiírja a 7-es szorzótáblát 1-től 10-ig!
7 x 1 = 7
7 x 2 = 14"""

def sixth_task():
    for x in range(1, 11):
        szam = x * 7
        print(f"{x} * 7 = {szam}")

sixth_task()
time.sleep(1)
print("\n")

"""4. Feladat: Számok visszafelé
Írj egy programot, amely kiírja a számokat 10-től 1-ig csökkenő sorrendben!
10
9
8"""

def seventh_task():
    for x in range(10, 0, -1):
        print(x)

seventh_task()
time.sleep(1)
print('\n')

"""
Feladat: Csillagok kirajzolása
Készíts egy programot, amely egy háromszöget rajzol csillagokból! Az első sorban 1
csillag, a másodikban 2, és így tovább, összesen 5 sorban.
*
**
***
"""
def eight_task():
    for x in range(1, 6):
        print("*" * x)

eight_task()
time.sleep(1)
print('\n')

"""
6. Feladat: Számok négyzetei
Írj egy programot, amely kiírja az 1-től 10-ig terjedő számok négyzeteit!
1 négyzete: 1
2 négyzete: 2
"""
def ninth_task():
    for x in range(1, 11):
        print(f"{x} négyzete: {x * x}")

ninth_task()