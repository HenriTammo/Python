f = open("skoorid.txt", "r")

nimed = list()  #teine võimalus kuidas luua listi peale []
skoorid = list()
#print(nimed)
mitu = int(f.readline())
for rida in f:
    nimi, skoor = rida.split(" ")
    nimed.append(nimi)
    skoorid.append(int(skoor))

mskoor = 0
jskoor = 0
kordm = 0
kordj = 0

for game in range(mitu):
    if nimed[game] == "m":
        mskoor = mskoor + skoorid[game]
        kordm = kordm + 1
    else:
        jskoor = jskoor + skoorid[game]
        kordj = kordj + 1
        
mskoor = mskoor/kordm
jskoor = jskoor/kordj

if mskoor > jskoor:
    print("mari oli parem")
else:
    print("jõri oli parem")
    
f.close()
                                                                                    