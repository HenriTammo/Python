import random
f = open("sorteerimine.txt", "w")
counter = 0
top = 0

for x in range(1000):
    f.write(str(random.randint(1, 100)) + "\n")
f.close()

r = open("sorteerimine.txt", "r")
lis = []
for x in r:
    x = x.strip()
    lis.append(int(x))
    
for x in lis:
    current = x
    if current >= top:
        top = current
        counter = counter + 1
print ("Suurim number on", top, "ja seda esines", counter, "korda")


