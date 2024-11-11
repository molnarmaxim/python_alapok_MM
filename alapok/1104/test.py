"""
A csoport:
Készítsünk programot, amely dinnyék csomagolásához végez számításokat. A
dinnyéket szalaggal kell átkötni úgy, hogy kétszer körbe érje őket, és a masni
készítéséhez számolunk még 60 cm-t. A program kérje be a dinnye átmérőjét, a
dinnyék számát, és a rendelkezésre álló szalag hosszát! Számítsa ki, és írja a
képernyőre, hogy a bekért számú dinnye csomagolásához hány méter szalagra van
szükség, valamint állapítsa meg, hogy elegendő szalagunk van-e a művelet
elvégzéséhez, és ezt is közölje a felhasználóval!
"""

import math
import time

print("🍉 Dinnye csomagolás")
time.sleep(0.5)
#Adat bekérés
atmero = float(input("Kérlek add meg a dinnyék átmérőjét (cm)! "))
dinnye_szam = float(input("Kérlek add meg a dinnyék számát! "))
szalag = float(input("Kérlek add meg hány méter szalagod van! "))

print(f"×---------------×\nÁltalad megadott adatok:\n- Átmérő: {atmero}cm\n- Dinnyék: {dinnye_szam}\n- Szalag: {szalag}m\n×---------------×")

kor = math.pi * atmero
szalag_kell = ( 2 * kor + 60 ) * dinnye_szam
szalag_kell_meter = szalag_kell / 100 

if szalag_kell_meter <= szalag:
    print(f"🎊 Van elegendő szalagod a becsomagoláshoz! Szükséges: {szalag_kell_meter:.2f}m")
else: 
    print(f"❌ Nincs elegendő szalagod a becsomagoláshoz! Szükséges: {szalag_kell_meter:.2f}m")
