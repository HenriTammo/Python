r = open("nädal4/test.txt", "r")
lis = []
for x in r:
    x = x.strip() # eemaldab \n
    x = x.replace(".", "") #kasutab replace funktsionaalsust et eemaldada punkt
    lis.append(int(x)) #lisame x listi ja muudame väärtuse numbriks
    
for x in lis:
    if x%2 == 0:
        print(x, "on paarisarv")
    else:
        print(x, "on paaritu arv")
