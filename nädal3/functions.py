import extensio

def summa(a, b):
    c = a + b
    return c

def lahutus():
    arv = 6 - 2
    return arv

def sisesta():
    a = int(input("Sisesta vanus" + "\n"))
    b = input("Sisesta nimi" + "\n")
    b = b.rstrip()
    print (a, b)
    return b

a = 2
b = 4
d = summa(a, b)
x = lahutus()
s = sisesta()
misc = extensio.other()
print (misc)
print(d)
print(x)