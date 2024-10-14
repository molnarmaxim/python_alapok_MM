# kommentként tartalmazza a program funkciójának leírását,
# konstansként tárolja PI értékét,
# egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
# kiszámolja és a képernyőre kiírja a kör kerületét és területét!
# [Megjegyzés] A szorzás jele: *

#Adatok
pi = 3.14
r = 5

#Képletek
kerulet = int(2 * r * pi)
terulet = (r * r) * pi

#Kiírás
print(f"Kerület: {kerulet}cm")
print(f"Terület: {terulet}cm2")

