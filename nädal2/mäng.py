import random
kasutaja = input("Mis on sinu nimi")

kontroll = True
while kontroll == True:
    relv = input("warrior, twosword, defender")
    turvis = input("light, medium, heavy")
    if (relv == "warrior" or relv == "twosword" or relv == "defender") and (turvis == "light" or turvis == "medium" or turvis == "heavy"):
        kontroll = False
    else:
        print("palun sisesta uuesti")
    
player = {
    "nimi" : kasutaja,
    "elud" : 50,
    "relv" : relv,
    "turvis" : turvis,
    "elu pott" : 2
    }
Diablo = {
    "nimi" : "Diablo",
    "elud" : 1500,
    "relv" : "põrgu küüned",
    "turvis" : "lohe nahk",
    "maagia" : "tõukab vastast"
    }

if turvis == "light":
    armor = 4
elif turvis == "medium":
    armor = 8
elif turvis == "heavy":
    armor = 16
    
combat = True
while combat == True:
    """print ("Kasutja lööb")
    Diablo["elud"] = Diablo["elud"] - random.randint(0, 10)
    print ("Diablo lööb, pane vaim valmis")
    player["elud"] = player["elud"] - random.randint(15, 25)"""
    if player["relv"] == "warrior":
        dmg = random.randint(8, 14)
    elif player["relv"] == "defender":
        dmg = random.randint(7,12)
    elif player["relv"] == "twosword":
        dmg = random.randint(10, 20)
    
    if dmg >= 11:    #tegelane ründab
        Diablo["elud"] = Diablo["elud"] - dmg
        print(Diablo["elud"])
    else:
        print("Diablo ei saanud haiget")
    
    
    if random.randint(0, 20) >= armor:    #Diablo ründab
        player["elud"] = player["elud"] - dmg
        print(player["elud"])
    else:
        print("Tegelane ei saanud haiget")
        
    
    if player["elud"] < 0:
        combat = False
        print("YOU DIED!")
print("Game over!")