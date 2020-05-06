from math import sin, cos, tan
import math
kujundr = ("ruut")
kujundo = ("romb")
arvud = [2, 5, 13, 25]
if kujundr == "ruut":
    a = arvud[0]
    ruutÜ = 4*a
    ruutP = a**2
    ruuduPD = a*math.sqrt(2)
    print (ruuduPD)
    ruuduD = (9*2)/2
if kujundo == "romb":
     a = arvud[2]
     b = arvud[1]
     h = arvud[3]
     rombÜ = 4*b
     h = a*(tan(180))
     rombP = b*h
thislist = [ruutÜ, ruutP, ruuduPD, ruuduD]
print (thislist)
thislist = [rombÜ, h, rombP]
print (thislist)