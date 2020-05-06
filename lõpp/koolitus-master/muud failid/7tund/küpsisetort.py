#Küpsisetordi tegemisel laotakse küpsised ristkülikukujulisele kandikule ja seda mitmes kihis, 
#nii, et igas kihis on sama palju küpsiseid. Küsida kasutajalt, mitu küpsist mahub kandikule laiuses
#ja mitu pikkuses ning kui mitme kihilist torti ta teha soovib. Seejärel küsida, kui mitu küpsist 
#on ühes pakis.
#Lõpuks väljastada, mitu küpsisepakki tuleb sellise tordi tegemiseks osta. NB! Eeldame, et poolikut küpsisepakki osta ei saa.
import math

küpsisepakk = int(input("kui palju küpseid on pakkis"))
küpsisetortpv = int(input("paremalt vasakule mitu rida küpsist mahub ritta"))
küpsisetortüa = int(input("ülevalt alla mitu küpsise rida mahub"))
küpsisetortk = int(input("mitu kihti soovid teha Küpsisetordile"))
pinnaküpsised = küpsisetortpv * küpsisetortüa
kokku = pinnaküpsised * küpsisetortk

if küpsisepakk > kokku:
    print("sulle piisab ühest pakkist")
else:
    mitu = kokku/küpsisepakk
    mitu = math.ceil(mitu) #math.ceil()ümardab üles alati
    print("sul läheb vaja", mitu, "pakki küpsiseid")