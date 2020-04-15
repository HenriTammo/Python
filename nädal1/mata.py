from math import sin, cos
import math
kujundr = ("ruut")
kujundo = ("romb")
if kujundr == "ruut":
    a = float(input("esimene arv"))
    ruutÜ = 4*a
    ruutP = a**2
    ruuduPD = a*math.sqrt(2)
    print (ruuduPD)
    ruuduD = (92)/2 #kas siia saab muidu 9 asemel kuidagi d panna
if kujundo == "romb":
     b = float(input("teine arv"))
     c = float(input("kolmas arv"))
     rombÜ = 4*b
     h = a*(sin(180))# siin on probleemi ei ole välja mõelnud (180 kraad)
     rombP = b*h
thislist = [ruutÜ, ruutP, ruuduPD, ruuduD]
print (thislist)
thislist = [rombÜ, h, rombP]
print (thislist)