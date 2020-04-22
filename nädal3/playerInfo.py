import random

def playerSetup():
    info = []
    kasutaja = input("mis on teie nimi")
    info.append(kasutaja)
    kontroll = True
    while kontroll == True:
        klass = input("warrior\ndefender\nberseker\nassassin")
        info.append(klass)
        relv = input("axe\nswordshield\ntwohandssword\ntwoswords")
        info.append(relv)
        turvis = input("leather\nlight\nmedium\nheavy")
        info.append(turvis)
        if (klass == "warrior" or klass == "defender" or klass == "berseker" or klass == "assassin") and (relv == "axe" or relv == "swordshield" or relv == "twohandssword" or relv == "twoswords") and (turvis == "leather" or turvis == "light" or turvis == "medium" or turvis == "heavy"):
            kontroll = False
        else:
            print("palun sisesta uuesti")
    return info

def armor(turvis):
    if turvis == "leather":
        armor = 2
    elif turvis == "light":
        armor = 4
    elif turvis == "medium":
        armor = 8
    elif turvis == "heavy":
        armor = 20
    return armor

def weapon(relv):
    if relv == "axe":
        tugevus = 25
    elif relv == "swordshield":
        tugevus = 14
    elif relv == "twohandssword":
        tugevus = 30
    elif relv == "twoswords":
        tugevus = 28
    return tugevus

def health(klass):
    if klass == "warrior":
        elud = 100    
    elif klass == "defender":
        elud = 150
    elif klass == "berseker":
        elud = 125
    elif klass == "assassin":
        elud = 75
    return elud


def dmg(klass):
    if klass == "warrior":
        dmg = random.randint(12, 25)
    elif klass == "defender":
        dmg = random.randint(4, 21) 
    elif klass == "berseker":
        dmg = random.randint(9, 20)
    elif klass == "assassin":
        dmg = random.randint(7, 24)
    return dmg