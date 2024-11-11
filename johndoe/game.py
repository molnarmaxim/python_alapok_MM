import math

atmero = float(input("Add meg a dinnye átmérőjét (cm): "))
darab_szam = int(input("Add meg a dinnyék számát: "))  
rendelkezésre_allo_szalag = float(input("Add meg a rendelkezésre álló szalag hosszát (m): "))  

kor = math.pi * atmero  
szalag_szukseges = (2 * kor + 60) * darab_szam 
szalag_szukseges_meter = szalag_szukseges / 100  

if szalag_szukseges_meter <= rendelkezésre_allo_szalag:
    print(f"Elég szalag van! {szalag_szukseges_meter:.2f} méter szükséges.")
else:
    print(f"Nem elég szalag! {szalag_szukseges_meter:.2f} méterre lenne szükség.")


szelesseg = float(input("Add meg a terület szélességét (m): ")) 
magassag = float(input("Add meg a terület magasságát (m): "))  
mar_vett_csempe = int(input("Hány csempét vásároltál már? "))  

csempe_terulet = 0.2 * 0.2  


terulet = szelesseg * magassag  


szukseges_csempe = terulet / csempe_terulet  


szukseges_csempe_tartalekkal = szukseges_csempe * 1.1  


szukseges_csempe_tartalekkal = math.ceil(szukseges_csempe_tartalekkal)

if mar_vett_csempe >= szukseges_csempe_tartalekkal:
    print(f"Elég csempe van! {szukseges_csempe_tartalekkal} csempe szükséges.")
else:
    print(f"Hiányzik {szukseges_csempe_tartalekkal - mar_vett_csempe} csempe!")
