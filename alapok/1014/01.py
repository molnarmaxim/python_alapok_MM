number = int(input("Kérlek adj meg egy páros számot! "))
number_paros = False


while number_paros == False:
    if number % 2 == 0:
        number_paros = True
        print("✅")
    else:
        number_paros = False
        print("❌")
        number = int(input("Kérlek adj meg egy páros számot! "))

