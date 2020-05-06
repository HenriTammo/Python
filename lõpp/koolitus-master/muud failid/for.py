for x in range(2, 6):
    print(x)
    
for y in range (2, 30, 3):
    print (y)
    
for z in "python":
    print (z)
    
for z in "python":
    if z == "p":
        print ("paabulind")
    elif z == "t":
        print ("troll")
    else:
        print(z)
        
thislist = ["amd", "intel", "nvidia"]
for x in thislist:
    print(x)

thislist = ["amd, intel, nvidia"]
for x in thislist:
    print(x)
    
for x in range(6):
    print(x)
else:
    print("sai tehtud")
    
number = 0
for x in range(10):
    number = number + 1
    if number > 5:
        print(number)
        
list1 = ("red", "green", "blue")
list2 = ("punane", "roheline", "sinine")
for x in list1:
    for y in list2:
        print (x, y)
        
list1 = ("2", "6", "12")
list2 = ("1", "3", "5")
for x in list1:
    for y in list2:
        print (x, y)
        
arv1 = 5
arv2 = 10
arv3 = 0
for x in range(arv1):
    for y in range(arv2):
        arv3 = arv3 + y
print (arv3)

list3 = []
for x in range(10):
    list3.append(x)
print(list3)

arv1 = 1
for x in range(20):
    if arv1%2 == 0:
        print ("arv jagub 2")
        arv1 = arv1 + 1
    else:
        arv1 = arv1 + 1
        
        
m = 30
thislist = []
for x in range(15):
    if m%2 == 0: 
        print ("arv jagub kahega", m)
        m = m + 3
    else:
        thislist.append(m)
        m = m + 5        
print (thislist)
        
        