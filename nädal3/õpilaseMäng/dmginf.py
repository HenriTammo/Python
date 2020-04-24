import random
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