"""0. Feladat: Számok kiírása
Írj egy programot, amely kiírja az 1-től 20-ig a számokat!
1
2
3
...
"""

import time

def first_task():
    szam = 1
    for szam in range(21):
        print(szam)
        szam += 1

first_task()
time.sleep(1)

def second_task():
    szam = 1
    for szam in range(21):
        print(szam, end="")
        szam += 1

second_task()