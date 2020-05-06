thisdict = {
    "brand" : "Ford mustang",
    "model" : "Elanor",
    "year" : 1965
    }
print(thisdict)

x = thisdict["model"]
print(x)#2

print(thisdict["model"])

thisdict["year"] = 1967
print(thisdict)

for x in thisdict:
    print(x)
    
for x in thisdict.values():
    print(x)
    
for x, y in thisdict.items():
    print(x, y)#kuidas printida muutuja ja väärtus.
    
if "model" in thisdict:
    print(thisdict["model"])

print(len(thisdict))

del thisdict["brand"]
print(thisdict)
#thisdict.clear()--kustudab kõik
mydict = thisdict.copy()
print(mydict)

thisdict["brand"] = "Ford mustang"
print(thisdict)

