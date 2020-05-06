import täring

def playerSetup():
    info = []
    kasutaja = input("mis on teie nimi")
    info.append(kasutaja)
    info.append("mõõk")
    info.append("nahkerüü")
    info.append(täring.d6Add12()) #vastupidavus
    info.append(täring.d6Add6())  #õnn
    info.append(täring.d6Add6())  #osavus
    return info
