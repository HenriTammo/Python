f = open("skoorid.txt", "r")

nimed = list() #teine võimalus kuidas luua listi peale []
skoorid = list()

mitu = int(f.readline())
for rida in f:
    nimi, skoor = rida.split(" ")
    nimed.append(nimi)
    skoorid.append(int(skoor))

mSkoor = 0
jSkoor = 0
kordm = 0
kordj = 0

for game in range(mitu):
    if nimed[game] == "M":
        mSkoor = mSkoor + skoorid[game]
        kordm = kordm + 1
    else:
        jSkoor = jSkoor + skoorid[game]
        kordj = kordj + 1
        
mSkoor = mSkoor/kordm
jSkoor = jSkoor/kordj

if mSkoor > jSkoor:
    print("Mari oli parem")
else:
    print("Jüri oli parem")
    
f.close()