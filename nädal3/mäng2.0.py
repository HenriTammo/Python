import random
import playerInfo

player = playerInfo.playerSetup()
print (player)

character = {
    "nimi" : player[0],
    "klass" : player[1],
    "elud" : 50 + playerInfo.health(player[1]),
    "relv" : playerInfo.weapon(player[2]),
    "turvis" : playerInfo.armor(player[3]),
    "elu pott" : 2
    }
Diablo = {
    "nimi" : "Diablo",
    "elud" : 1500,
    "relv" : "põrgu küüned",
    "turvis" : "lohe nahk",
    "maagia" : "2xtugevusrünnak"
    }
    
combat = True
while combat == True:
    
    dmg = playerInfo.dmg(character["klass"])

    if dmg >= 19:
        Diablo["elud"] = Diablo["elud"] - dmg
        print("Diablo elud", Diablo["elud"])
    else:
        print("Diablo ei saanud haiget")
        
    if random.randint(0, 20) >= character["turvis"]:           #Diablo ründab
        character["elud"] = character["elud"] - dmg
        print("player elud", character["elud"])
    else:
        print("klass ei saanud haiget")
    
    if character ["elud"] < 50:#poolik
        lisa = "elu pott"
        print("elu pott")
        
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