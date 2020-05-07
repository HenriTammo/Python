def store1(gold):
    boughtList = []
    storeDict = {
        "asi1" : 3,
        "asi2" : 65,
        "asi3" : 6
    }
    store = True
    while store == True:
        print ("Teretuleamst poodi \n")
        print ("Meil on pakkuda", storeDict)
        soov = input("sisesta mida osta tahad")
        for x in storeDict:
            if soov == x:
                if gold < storeDict.get(x):
                  print ("pole piisavalt kulda")
                else :
                    boughtList.append(x)
                    gold = gold - storeDict.get(x)
                    del storeDict[x]
                soov = input("soovid veel y/n")
                if soov == "n":
                    store = False
                break
            else:
                print("Ei leidnud soovitud toodet")
            
    return boughtList, gold

    