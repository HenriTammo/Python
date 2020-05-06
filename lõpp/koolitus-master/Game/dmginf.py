import random
def dmg(klass):
    if klass == "warrior":
        dmg = random.randint(47, 75)
    elif klass == "defender":
        dmg = random.randint(44, 65) 
    elif klass == "berseker":
        dmg = random.randint(46, 67)
    elif klass == "assassin":
        dmg = random.randint(45, 72)
    return dmg
    