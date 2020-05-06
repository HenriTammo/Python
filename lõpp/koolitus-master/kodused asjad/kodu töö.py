"""import math
a = 100
c = a*math.sqrt(4)
print (c)"""
"""a = float(input("Sisesta esimene arv: "))
b = float(input("sisesta teine arv: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a*0.25)"""

"""a = 8
b = 9
if a == b:
    print("Arvud on võrdsed")
else:
    print("Arvud on erinevad")
if a > b:
    print("Esimene arv on suurem")
else:
    print("Teine arv on suurem")
from math import sin, cos, pi
print(pi)
print(cos(0.5))
x = sin(4)
print(x)
print(round(x,2))"""

"""from turtle import *
forward(100)
left(90)
forward(100)
right(90)
backward(100)
left(90)
backward(100)
left(135)
backward(141)
left(90)
backward(70)
left(90)
backward(70)
left(90)
backward(141)"""

"""#aeg = float(input("Mitu tundi kulus sõiduks? "))
aeg = float(input("Mitu tundi kulus sõiduks: "))
#teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid: "))
kiirus = aeg / teepikkus

print("Sinu kiirus oli " + str(kiirus) + " km/h")"""

"""#bol = True
bol = False
fal = False
if bol == True:
    print("bol on tõene")
#elif bol == False:
elif fal == True:    
    print("bol pole tõene")
elif fal == False:
    print("fal on false")
else:
    print("kõik on vale")"""
    
"""a = 5
b = 6
c = 10

#if a < b and c > a:
if c < b and c > a:
    print ("c on kõige suurem")
#elif a > b or c > b: # lõpmatuseni võid kirjutada
   # print("b ei ole kõige suurem")
elif a > b or (a == 5 and b == 6):
    print ("a on 5 ja b on 6")"""

"""a = 20
b = 40
c = 100
d = 20
if a >= d:#vastupidine oleks <=
    print("a on suurem või võrdne d")
    if a <= c:
        c = c- a
        print("c on suurem a-st", c, "võrra")
        
string = "Tere"
if string == "Tere":
    print (string, "Maailm")"""

"""kujund = input("kolmnnurk või ristkülik")
#if kujund != "kolnurk" and kujund != "ristkülik":
   # print ("sisestas vale sõna")
if kujund == "kolmnurk":
    a = float(input("Esimene arv"))
    b = float(input("teine arv"))
    c = float(input("kolmas arv"))
    kolmnurkÜ = a+b+c
    kolmnurkP = (a*b)/2
    print (kolmnurkÜ, kolmnurkP)
elif kujund == "ristkülik":
    a = float(input("Esimene arv"))
    b = float(input("teine arv"))
    ristkülikÜ = (a+b)*2
    ristkülikP = a*b
    print (ristkülikÜ, ristkülikuP)
else:
    print ("sisestas vale sõna")"""

"""thislist = [1, 2, 3, "neli"]
    # koht  0, 1, 2, 4
print (thislist[1])
print (thislist[0:2])
print (thislist[0], thislist[3])
thislist.append("auto")
print (thislist)
thislist.insert(2, "mootor")#tahab positsiooni
print (thislist)
thislist.remove(2)#tahab väärtust
print (thislist)
thislist.pop(1)# võidtäpsustada poitsiooni
print(thislist)
#thislist.clear()
#print(thislist)
print (len(thislist))
list1 = [1, 2]
list2 = [3, 4]
list3 = list1 + list2
print(list3)

#siinalgavadd settid
sett = {1, 2, 3} #altg+ 7, 0 = {}
#välja pritimine nagu listis
print (sett)

sett.add("orange")
sett.add("orange")# ei luba duplikaate
sett.add("black")
print (sett)
sett.discard("orange")
print(sett)
sett1 = {1}
sett2 = {2}
sett3 = sett1.union(sett2)
print(sett3)

import random
x = random.randint(1, 6)
print(x)"""

"""thislist = [1, 2, 3]
thislist2 = [9, 8, 7, 6, 5, 4]
#if (len(thislist)) == 3:
if (len(thislist)) == 4:
    thislist.append(4)
    print(thislist)
elif(len(thislist)) > 7:
    thislist.pop(0)
    print(thislist)
elif (len(thislist)) < 5 < (len(thislist2)):
    print (thislist + thislist2)
a = thislist[1]
print (a)"""
    
    
    