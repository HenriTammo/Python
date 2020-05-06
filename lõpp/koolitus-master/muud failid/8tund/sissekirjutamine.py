f = open("muud failid/8tund/sissekirjutamine.txt", "w") #faili kirjutamine
arv = 300

for x in range(101):
    f.write(str(arv) + "." + "\n")
    arv = arv + 1