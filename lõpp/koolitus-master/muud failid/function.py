import extensionb

def summa(a, b):
    c= a + b
    return c

def lahutus():
    arv = 6 - 2
    return arv

def sisesta():
    a = int(input("sisesta vanus" + "\n"))
    b = input("sisesta nimi" + "\n")
    b=b.rstrip()
    print (a, b)
    
a = 2
b = 4
d = summa (a, b)
x= lahutus()
#s = sisesta()
misc = extensionb.other()
print(misc)
print(d)
print(x)