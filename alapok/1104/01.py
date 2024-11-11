"""1. Egyszerű számbekérő
Kérj be egy számot a felhasználótól, és döntsd el, hogy páros vagy páratlan. Írd ki az eredményt!”””
"""
def elsofeladat():
    number = int(input("Kérlek adj meg egy számot! "))

    if number % 2 == 0:
        print("A szám páros")
    elif number % 2 != 0:
        print("A szám páratlan")
    else: print("Váratlan hiba történt!")

"""
2. Összegszámítás
Kérj be egy egész számot, és számítsd ki az 1-től a megadott számig terjedő egész számok összegét.
"""
def masodikfeladat():
    number = int(input("Kérlek adj meg egy számot! "))
    default_number = 1


    for x in range(default_number + 1, number):
        print(default_number + number)
        default_number = default_number + 1 



"""
3. Számok listázása és összegzése
Írj egy programot, amely bekér  n számot a felhasználótól, majd egy while ciklussal megkérdezi a felhasználót, hogy szeretne-e újabb számot megadni. Addig folytassa a program a számok bekérését, amíg a felhasználó igennel válaszol. A program végén jelenítse meg a bekért számok összegét.
b) jelenítse meg a bekért számokat (lista használata)


"""
def harmadikfeladat():
    num_list = []
    current_number = 0

    n = int(input("Hány számot szeretnél megadni? "))

    for x in range(n):
        n = 1
        number = int(input(f"{n}. Kérlek adj meg egy számot: "))
        num_list.append(number)
        current_number = current_number + number
        n += 1



    wantmore = True
    while wantmore:
        wantinput = input("Szeretnél hozzáadni újabb számot? ")
        if wantinput == "y":
            print("igen")
            addednumber = int(input("Kérlek adj meg egy számot akkor: "))
            num_list.append(addednumber)
            current_number = current_number + addednumber
        elif wantinput == "n": 
            wantmore = False
            print("nem")

    print(num_list)
    print(current_number)

"""
4. Két szám közötti számok
Kérj be két számot a felhasználótól (a és b). Írasd ki az összes számot a és b között.
b) Ha a nagyobb, mint b, akkor csökkenő sorrendben írasd ki őket.
"""
def negyedikfeladat():
    num1 = int(input("Kérlek add meg az első számot! "))
    num2 = int(input("Kérlek add meg a második számot! "))

    if num1 < num2:
        num = num1
        for i in range(num1, (num2 + 1)):
            print(num)
            num += 1
    elif num1 > num2:
        num = num1
        for i in reversed(range(num2, (num1 + 1))):
            print(num)
            num -= 1


"""
5. Egyszerű jelszókérés
Készíts egy programot, amely egy előre meghatározott jelszót vár el a felhasználótól. A program addig kérdez, amíg a helyes jelszót meg nem adják. Ha eltalálja a jelszót, jelenjen meg egy üzenet, hogy „Sikeres belépés”.
"""
def otodikfeladat():
    jelszo = "kaki"

    rosszJelszo = True

    while rosszJelszo:
        userJelszo = input("[Belépés] Kérlek add meg a jelszavad! ")
        if userJelszo == "kaki":
            print("[Belépés] Sikeres belépés!")
            rosszJelszo = False
        else:
            print("[Belépés] Helytelen jelszó! Kérlek próbáld újra")


"""
6. Szorzótábla
Írasd ki egy adott szám szorzótábláját 1-től 10-ig. Például, ha a felhasználó 5-öt ad meg, akkor az eredmény legyen:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
"""
def hatodikfeladat():
    number = int(input("Kérlek adj meg egy számot! "))
    current = 1

    for x in range(1, 11):
        eredmeny = current * number
        print(f"{current} × {number} = {eredmeny}")
        current += 1

"""
7. Maximum keresés lista elemeiben
Készíts egy programot, amely bekér 5 számot a felhasználótól, és kiírja a legnagyobb számot. A programban használj egy for ciklust a számok bekérésére, és egy if feltételt a legnagyobb szám megkeresésére.
"""
def hetedikfeladat():
    print("x")

"""
8. Prímszám ellenőrzés
Kérj be egy számot, és döntsd el, hogy prímszám-e vagy sem. A program akkor jelezze, ha prímszámot talált, és akkor is, ha nem az.
"""

def nyolcadikfeladat():

    num = int(input("Adj meg egy számot! "))

    isPrime = False

    if num == 0 or num == 1:
        print(num, "nem egy prímszám")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                isPrime = True
                break

        if isPrime:
            print(num, "nem egy prím szám")
        else:
            print(num, "egy prímszám")
"""
9. Piramis rajzolása csillagokkal
Kérj be egy számot, amely megadja a piramis magasságát, majd rajzolj ki egy csillagpiramist ennek megfelelően. Például egy 5 magas piramis:
   *
   ***
  *****
 *******
*********


"""
def kilencedikfeladat():
    def piramis(magassag):
        for i in range(magassag):
            koz = ' ' * (magassag - i - 1)
            csillag = '*' * (2 * i + 1)
            print(koz + csillag)

    magassag = int(input("Add meg a piramis magasságát: "))
    piramis(magassag)

"""
10. Szorzótábla mátrix formában
Készíts egy programot, amely kiírja az 1-től 10-ig terjedő szorzótáblát egy 10x10-es mátrix formájában. Minden sor egy-egy i értéket képviseljen, minden oszlop pedig egy j értéket, és az i * j szorzatot jelenítse meg.
"""

def tizedikfeladat():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:3}", end=" ")
        print()

def run():
    elsofeladat()
    masodikfeladat()
    harmadikfeladat()
    negyedikfeladat()
    otodikfeladat()
    hatodikfeladat()
    hetedikfeladat()
    nyolcadikfeladat()
    kilencedikfeladat()
    tizedikfeladat()


run()