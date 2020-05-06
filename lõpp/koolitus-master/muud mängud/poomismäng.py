user = input("sisesta nimi")
print ("Tere tulemast surnuaeda", user)
game = True
elu = 10
sõna = []
for x in "raamatukoguhoidija":
         #012345678901234567
    sõna.append(x)
#print (len(sõna))
sõnaspikker = []
for x in range(18):
    sõnaspikker.append("_")
while game == True:
    if elu == 0:
        break
    print (sõnaspikker)
    pakkumine = input("paku mingi täht")
    if pakkumine == "r":
        sõnaspikker.insert(0, "R")
    if pakkumine == "a":
        sõnaspikker.insert(1, "A")
        sõnaspikker.insert(2, "A")
        sõnaspikker.insert(4, "A")
        sõnaspikker.insert(17, "A")
    if pakkumine == "m":
        sõnaspikker.insert(3, "M")
    if pakkumine == "t":
        sõnaspikker.insert(5, "T")
    if pakkumine == "u":
        sõnaspikker.insert(6, "U")
    if pakkumine == "k":
        sõnaspikker.insert(7, "K")
    if pakkumine == "o":
        sõnaspikker.insert(8, "O")
        sõnaspikker.insert(12, "O")
    if pakkumine == "g":
        sõnaspikker.insert(9, "G")
    if pakkumine == "u":
        sõnaspikker.insert(10, "U")
    if pakkumine == "h":
        sõnaspikker.insert(11, "H")
    if pakkumine == "i":
        sõnaspikker.insert(13, "I")
        sõnaspikker.insert(15, "I")
    if pakkumine == "d":
        sõnaspikker.insert(14, "D")
    if pakkumine == "j":
        sõnaspikker.insert(16, "J")
    break