import math
import sys
"""bol = False
fal = False
if bol == True:
    print("bol on tõene")
elif fal == True:
    print ("bol ei ole tõene")
elif fal == False:
    print ("fal on false")
else:
    print ("kõik on vale")"""
kujund = "a"
if kujund != "kolmnurk" and kujund != "ristkülik":
    sys.exit("vale")

a = 5
b = 6
c = 10

if c < b and c > a:
    print ("c on kõige suurem")
elif a > b or (a == 5 and b == 6):
    print ("a on 5 ja b on 6")
    
a = 100
c = a*math.sqrt(2)
print (c)


a = 20
b = 40
c = 100
d = 20

if a >= d: #vastupidine oleks <=
    print ("a on suurem või võrdne d")
    if a <= c:
        c = c - a
        print ("C on suurem A-st ", c, " võrra")
    
string = "tere"



