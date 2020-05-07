import math
import vastaseinf
#import vastused
import Backpack
import random
import playerInf
import täring
import store

playerInfo = playerInf.playerSetup()
enemyInfo  = vastaseinf.NÕELUSS()
newItems, newGold = store.store1(100)
items = ["toiduained", "joogipoolis"]
items = Backpack.update(items, newItems)

player = {
    "nimi" : playerInfo[0],
    "relv" : playerInfo[1],
    "turvis" : playerInfo[2],
    "kott" : items,
    "vastupidavus" : playerInfo[3],
    "õnn"  : playerInfo[4],
    "osavus" : playerInfo[5],
    "raha" : newGold
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
        print("you win")

#player["kott"] = bacpack.bp(player("kott"), items)
