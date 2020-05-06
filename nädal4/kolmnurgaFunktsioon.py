def kolnurga_pindala(a, b): #annan argumentideks kaasa a ja b
    p = (a*b)/2
    return p #return tagastab funktsioonist väärtuse

a = int(input("Esimene külg"))
b = int(input("Teine külg"))
c = kolnurga_pindala(a, b)
print (c)