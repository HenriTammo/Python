thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
    }
print(thisdict)

#x = thisdict["model"]
print(thisdict["model"])

thisdict["year"] = 1967
print(thisdict)

for x in thisdict:
    print(x)
    
for x in thisdict.values():
    print(x)

for x, y in thisdict.items():
    print(x, y)
    
if "model" in thisdict:
    print(thisdict["model"])
    
print(len(thisdict))

del thisdict["year"]
print(thisdict)
#thisdict.clear()

mydict = thisdict.copy()
print(mydict)

thisdict["year"] = 1964
print(thisdict)

