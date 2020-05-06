import math
import vastaseinf
#import vastused
#import backpack
import random
import playerInf
import täring

playerInfo = playerInf.playerSetup()
enemyInfo  = vastaseinf.NÕELUSS()

player = {
    "nimi" : playerInfo[0],
    "relv" : playerInfo[1],
    "turvis" : playerInfo[2],
    "kott" : ["toiduained", "joogipoolisega"],
    "vastupidavus" : playerInfo[3],
    "õnn"  : playerInfo[4],
    "osavus" : playerInfo[5],
    "raha" : 30
    }

enemy = {
    "vastupidavus" :enemyInfo[0],
    "osavus" :enemyInfo[1],
    "drop" : enemyInfo[2]
    }

    #combat kuhu liigud
#ask = int(input("sisesta järgnev tee konna nr")) --- seda pole vaja

combat = True
while combat == True:
    playerHit = täring.d6korda2() + player["osavus"]
    enemyHit = täring.d6korda2() + enemy["osavus"]
    if playerHit == enemyHit:
        print ("Lõite üksteisest mööda")
    elif playerHit > enemyHit:
        enemy["vastupidavus"] = enemy["vastupidavus"] - 2
    else:
        player["vastupidavus"] = player["vastupidavus"] - 2

    if player["vastupidavus"] == 0:
        print("""
         _____
        / ____|
        | |  __  __ _ _ __ ___   ___    _____   _____ _ __
        | | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
        | |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |
        \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|
        """)
        combat = False
    elif enemy["vastupidavus"] == 0:
        combat = False
        if enemy["drop"] == "mitte midagi":
            print("vastasel polnud aardeid")
        else:
            if isinstance(enemy["drop"], int):
                player["raha"] = player["raha"] + enemy["drop"]
                print("Sul on nüüd", player["raha"], "kulda")
            else:
                player["kott"].append(enemy["drop"])
                print("Sinu seljakotis on nüüd", player["kott"])

#player["kott"] = bacpack.bp(player("kott"), items)
