from math import sin, cos
import math
kujund = input("ruut või romb")
arvud = [2, 5, 13, 25]
if kujund == "ruut":
     a = arvud[0]
     ruutÜ = 4*a
     ruutP = a**2
     ruuduPD = a*math.sqrt(2)
     print (ruuduPD)
     ruuduD = (9*2)/2
elif kujund == "romb":
     a = arvud[0]
     b = arvud[1]
     h = arvud[3]
     rombÜ = 4*b
     h = a*(sin(180))
     rombP = b*h
thislist = [ruutÜ, ruutP, ruuduPD, ruuduD, rombÜ, h, rombP]
print (thislist)

