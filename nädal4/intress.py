import math
pangaArve = float(input("Kui palju raha on arvel"))
intress = float(input("Sisesta oma intress"))
aeg = 5
for x in range(aeg):
    pangaArve = pangaArve + (intress/100) * pangaArve #arvutus arvutab välja intressiga juurde tuleva summa ning lisab selle algsele summale juurde

print("5 aastaga kogud", int(pangaArve))