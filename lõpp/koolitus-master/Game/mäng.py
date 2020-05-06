import random
import playerinf
import dmginf
import vastaseinf
import time

player = playerinf.playerSetup()
print (player)


character = {
    "nimi" : player[0],
    "klass" : player[1],
    "elud" : 100 + playerinf.health(player[1]),
    "relv" : playerinf.weapon(player[2]),
    "turvis" : playerinf.armor(player[3]),
    "elu pott" : 4
    }

Diablo = {
    "nimi" : "Diablo",
    "elud" : 1500,
    "relv" : vastaseinf.weapon("põrgu küüned"),                #100 dmg
    "turvis" : vastaseinf.armor("lohe nahk"),                  # lisab 45 armorit
    "maagia" : vastaseinf.magics("2xtugevusrünnak")            #kui eulud on all 100
    }
   
combat = True
while combat == True:    

    dmg = dmginf.dmg(character["klass"])
    dmgDiablo = random.randint(10, Diablo["relv"])
    dmgmagic = random.randint(10, Diablo["maagia"])
  
    if dmg >= Diablo["turvis"]:                                              #player ründab
        Diablo["elud"] = Diablo["elud"] - dmg
        print("Diablo elud", Diablo["elud"])
    else:
        print("Diablo ei saanud haiget")

    #time.sleep(2)    

    if Diablo["elud"] < 100:
        if dmgmagic >=character["turvis"]:
            character["elud"] = character["elud"] - dmgmagic
            print("sinu elud", character["elud"]) 

    elif dmgDiablo >=character["turvis"]:           #Diablo ründab
        character["elud"] = character["elud"] - dmgDiablo
        print("Sinu elud", character["elud"])
    else:
        print("Sa ei saanud haiget")    	                  #klass ei saanud haiget
    
   # time.sleep(2)    

    if character ["elud"] < 50:                              
        if character["elu pott"] > 0:                         
            character["elud"] = character["elud"] + 100
            character ["elu pott"] = character["elu pott"] - 1

    if character["elud"] < 0:
        combat = False
        print("You DIED!")
    if Diablo["elud"] < 0:
        combat = False
        print("Mission completed!")
print("""
   _____
  / ____|
 | |  __  __ _ _ __ ___   ___    _____   _____ _ __
 | | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |
  \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|
""")