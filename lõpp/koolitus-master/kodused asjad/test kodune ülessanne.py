from math import sin, cos
import math
kujundr = ("ruut")
kujundo = ("romb")
a = float(input("esimene arv"))
b = float(input("teine arv"))
c = float(input("kolmas arv"))
if kujundr == "ruut":
     ruutÜ = 4*a
     ruutP = a**2
     ruuduPD = a*math.sqrt(2)
     ruuduD = (9*2)/2 #kas siia saab muidu 9 asemel kuidagi d panna
elif kujundo == "romb":
     rombÜ = 4*b
     h = a*(sin(180))# siin on probleemi ei ole välja mõelnud (180 kraad)
     rombP = b*h
     thislist = [ruutÜ, ruutP, ruuduPD, ruuduD, rombÜ, h, rombP]
     print (thislist)