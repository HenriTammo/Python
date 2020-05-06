from math import sin, cos, pi
import math
kujund = input("ruut või romb")
if kujund == "ruut":
    a = float(input("Esimene arv"))
    ruutÜ = 4a
    ruutP = a**2
    ruuduPD = amath.sqrt(2)
    print (ruuduPD)
    ruuduD = (9*2)/2 #kas siia saab muidu 9 asemel kuidagi d panna
    print (ruutÜ, ruutP, ruuduD, ruuduPD)
    # välja kirjutades ei sa aru kust see esimene nr tuleb
elif kujund == "romb":
    b = float(input("Esimene arv"))
    c = float(input("teine arv"))
    rombÜ = 4b
    h = a(sin(180))# siin on probleem ei ole välja mõelnud (180 kraad)
    rombP = bh
    print (rombÜ, rombP, h)
else:
    print ("sisestas vale sõna")