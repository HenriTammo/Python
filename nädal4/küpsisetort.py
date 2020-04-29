import math
ktr = int(input("Mitu küpsist mahub paremalt vasakule"))
ktt = int(input("Palju ülevalt alla")) #arvestab ilma ridadadeta
kõrgus = int(input("Mitme kihine tort tuleb"))
pakkis = int(input("mitu küpsist pakkis on"))

pinnaKüpsised = ktr*ktt

Kokku = pinnaKüpsised*kõrgus

if pakkis > Kokku:
    print("Sulle piisab ühest pakkist")
else:
    mitu = Kokku/pakkis
    mitu = math.ceil(mitu) #math.ceil() ümardab numbri üles alati
    print ("Sul läheb vaja", mitu, "pakki küpsiseid")