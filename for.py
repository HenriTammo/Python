for x in range(2, 6):
    print (x)
    
for y in range(2, 30, 3):
    print (y)
    
for z in "python":
    if z == "p":
        print ("paabulind")
    else:
        print (z)

thisList = ["amd", "intel", "nvidia"]
for x in thisList:
    print (x)
    
for x in range(6):
    print(x)
else:
    print("sai tehtud")
    
number = 0
for x in range(10):
    number = number + 1
    if number > 5:
        print(number)

list1 = ["red", "green", "blue"]
list2 = ["car", "phone", "house"]
for x in list1:
    for y in list2:
        print(x, y)
        
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
        print ("arv jagub kahega")
        arv1 = arv1 + 1 
    else:
        arv1 = arv1 + 1