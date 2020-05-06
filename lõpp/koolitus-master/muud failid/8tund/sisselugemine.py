#Kirjutage programm, mis loeb antud failist ükshaaval arve ning kuvab iga arvu 
#kohta ekraanile info, kas tegemist oli paaris või paaritu arvuga.



r = open("muud failid/8tund/sissekirjutamine.txt", "r")
lis = []
for x in r:    # üks haaval võtab ridasi
    x = x.strip() # eemaldab \n
    x = x.replace(".","") #eemaldame punkti
    lis.append(int(x)) # lisame x listi  ja muudame väärtuse nubmriks
    
for x in lis:
    if x%2 == 0: 
       print(x, "on paaris arv")
    else:
        print(x, "pole paaris arvud")