# Összehasonlító operátorok
# ==	egyenlő
# !=	nem egyenlő
# <	kisebb
# >	nagyobb
# <=	kisebb vagy egyenlő
# >=	nagyobb vagy egyenlő
# Logikai operátorok
# and	és
# or	vagy
# not	nem


# x = int(input("Kérlek adj meg egy egész számot! "))
#
# if x % 2 == 0 and x > 0:
#     print("A szám páros és pozitív.")
# elif x % 2 != 0 and x < 0:
#     print("A szám páratlan és negatív.")
#
#

question1 = str(input("Henrik jön ma kosarazni (Igen/Nem)? "))
question2 = str(input("Hanna jön ma kosarazni (Igen/Nem)? "))

if question1 == "Igen" and question2 == "Igen":
    print("Mindketten jönnek kosarazni.")
elif question1 == "Nem" and question2 == "Nem":
    print("Egyikük sem jön kosarazni")
elif question1 == "Nem" and question2 == "Igen":
    print("Hanna ma jön kosarazni")
elif question1 == "Igen" and question2 == "Nem":
    print("Henrik ma jön kosarazni")
else:
    print("Hiba történt")




