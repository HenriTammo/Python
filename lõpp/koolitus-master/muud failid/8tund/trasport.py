#Olgu meil vaja transportida teatud arv inimesi bussidega, milles on teatud arv kohti. 
#Mitu bussi on vaja selleks, et kõik inimesed kohale saaksid ja mitu inimest on viimases
#bussis (eeldusel, et eelmised on kõik täiesti täis)? Kirjutage programm, mis küsib inimeste arvu 
#ja busside suuruse ning lahendab seejärel selle ülesande.

#Testige oma programmi muuhulgas järgmiste algandmetega:

#inimeste arv: 60, kohtade arv: 40
#inimeste arv: 80, kohtade arv: 40
#inimeste arv: 20, kohtade arv: 40
#inimeste arv: 40, kohtade arv: 40
#kokku
#inimeste arv: 200   
import math

inimene = int(input("Mitu inimest ootab bussi"))
buss = int(input("mitu kohta on 1 bussis"))

if inimene < buss:
    print("piisab ühest bussist")
elif inimene == buss:
    print("inimesed mahuvad täpselt")
elif inimene > buss:
    arv = inimene/buss
    arv = math.ceil(arv)
    print ("läheb vaja", arv, "busse")
