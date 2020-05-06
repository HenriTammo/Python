x = 1
while x <10:
    print (x)
    x = x + 1

boolen = True
while boolen == True:
    print ("vastab tõele")
    boolen = False
    
x = 1    
while x < 5:
    print(x)
    x = x + 1
else:
    print ("x on liiga suur")
    
y = 1
boolen2 = True
while boolen2 == True:
    print (y)
    y =y + 1
    if y == 10:
        print("y muutus liiga suureks")
        boolen2 = False
        
z = 1
thislist = []
while z < 10:
    thislist.append(z)
    z = z + 1
print (thislist)

n = 1
thislist = []
while n < 10:
    thislist.append(n)
    n = n + 1
print  (thislist)

n = 6
n = n%2
print (n) # kui tuleb 0, siis jagub täpselt


m = 25
thislist = []
while m > 10:
    print (m)
    m = m - 1
    if m%2 == 0:
        thislist.append(m)
print (thislist)