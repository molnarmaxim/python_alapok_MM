

def task():
    darab_karakter = 1
    sor = 1
    mennyiseg = int(input("Kérlek adj meg egy páros számot! "))
    if mennyiseg % 2 == 0:
        while sor <= mennyiseg:
            oszlop = 1
            while oszlop <= darab_karakter:
                print('O ', end='')
                oszlop += 1
            print('')
            darab_karakter += 1
            sor += 1
        darab_karakter -= 1
        sor = 1
        while sor <= mennyiseg:
            oszlop = 1
            while oszlop <= darab_karakter:
                print('O ', end='')
                oszlop += 1
            print('')
            darab_karakter -= 1
            sor += 1
    else:
        print("Kérlek adj meg egy páros számot!")
        task()

task()