user = input("Sisesta nimi")
print ("Tere tulemast surnuaeda", user)

elud = 10
sõnaSpikker = []
sõna = []
test = ""

for x in "raamatukoguhoidija":
    sõna.append(x)

for x in range(18):
    sõnaSpikker.append("_")
    
while elud > 0:
    print (sõnaSpikker)
    asukoht = 0
    pakkumine = input("Paku mingi täht")
    for x in sõna:
        täht = x
        if pakkumine == täht:
            sõnaSpikker[asukoht] = pakkumine
            asukoht = asukoht + 1
        else:
            elud = elud - 1
            print ("seda tähte ei ole")
            asukoht = asukoht + 1
print ("mäng läbi")
