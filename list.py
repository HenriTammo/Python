"""thisList = [1, 2, 3, "neli"]
print (thisList[0:2])
print (thisList[0], thisList[2]) #eraldi välja kutsumine
thisList.append("auto")
print (thisList)
thisList.insert(1, "mootor")#tahab positsiooni
print (thisList)
thisList.remove("neli")#Tahab väärtust
print (thisList)
thisList.pop()#Võid täpsustada positsiooni
print (thisList)
#thisList.clear()
#print (thisList)
print (len(thisList))
list1 = [1, 2]
list2 = [3, 4]
list3 = list1 + list2
print (list3)


#siin algavad settid
sett = {1, 2, 3}
#välja printimine nagu listis
print (sett)
#for x in sett:
    #print (x)
#for tsükklist lähemalt järgmione tund
sett.add("orange")
sett.add("orange")#ei luba duplikaate
sett.add("tomato")
print (sett)
sett.discard("orange")
print (sett)
sett1 = {1}
sett2 = {2}
sett3 = sett1.union(sett2)
print (sett3)

import random
x = random.randint(1, 6)
print (x)"""

thisList = [1, 2, 3]
thisList2 = [4, 5, 6, 7, 8, 9]
if (len(thisList)) == 4:
    thisList.append(4)
    print(thisList)
elif (len(thisList)) >= 7:
    thisList.pop(0)
    print(thisList)
elif (len(thisList)) < 5 < (len(thisList2)):
    print (thisList + thisList2)

a = thisList[1]
print (a)
