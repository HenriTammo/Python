sõna = []
for x in "raamatukoguhoidija":
    sõna.append(x)
sõnaSpikker = []
for x in range(14):
    sõnaSpikker.append("_")

inp = input("täht")
test = ""
asukoht = 0
for x in sõna:
    täht = x
    if inp == täht:
        sõnaSpikker.insert(asukoht, inp)
    asukoht = asukoht + 1

print (sõnaSpikker)
        