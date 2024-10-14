# szam = int(input("Kérlek adj meg egy egész számot: "))
# if szam < 0:
#     print("Az általad megadott szám negatív")
# elif szam == 0:
#     print("Az általad megadott szám nulla")
# else:
#     print("Az általad megadott szám pozitív")
# print("Program vége")

def task():
    response = str(input("Jó napod volt? "))
    response_lower = response.lower()
    if response_lower == "igen":
        print("Örülök, hogy jó napod volt!")
    elif response_lower == "nem":
        print("Sajnálom, mesélnél kicsit többet róla?")
    else:
        print("Sajnos nem tudom értem a válaszodat, kérlek az alábbi két lehetőség közül válassz:\n - Igen\n - Nem\n")
        print("Próbáld újra!")
        task()
task()