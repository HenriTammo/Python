import math

#Kirjutage programm, mis küsib kasutajalt tema pangaarvel olevat summat ning intressi protsenti, 
#mida pank talle igal aastal maksab. 
#Vastuseks peab programm väljastama pangaarvel oleva summa 5 aasta pärast.

pangaArve = float(input("palun sisesta panga arve summa")) #kasutaja sisestus
interss = float(input ("sisesta oma kuine interss"))
aeg = 5
for x in range(aeg):
    pangaArve = pangaArve + (interss/100) * pangaArve #arvutus arvutab välja intressiga juurde tuleva summa ning lisab algsele summale juurde
print("5 aastaga kogud", int(pangaArve))
