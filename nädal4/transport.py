import math
inimesed = int(input("Palju inimesi on?"))
buss = int(input("Mitu kohta on bussis?"))

if inimesed < buss:
    print("Piisab ühest bussist")
elif inimesed == buss:
    print("Inimesed mahuvad täpselt ühte bussi")
elif inimesed > buss:
    arv = inimesed/buss
    arv = math.ceil(arv)
    print("Läheb vaja", arv, "busse")