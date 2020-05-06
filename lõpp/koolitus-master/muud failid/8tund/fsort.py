#Kirjutage funktsioon, mis võtab argumendiks täisarvude listi, ning tagastab, mitu elementi 
#antud listis olid paarisarvud.

def sorteerimine(lis): #(pole vahet mis siin sees on kirjutatud)
    kokku = 0
    for x in lis:
        if x%2 == 0: # kogu süsteem saab siit alguse
            kokku = kokku + 1 #lisab alati ühe juurde kui arv on paaris
            print(x, "paaris")
        else:
            print(x, "oli paaritu")
        
    return kokku
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arv = sorteerimine(lis)
print (arv)