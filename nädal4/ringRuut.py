import math
import random
diameeter = float(input("sisesta ringi diameeter"))
pindala = (diameeter**2)/2
a = math.sqrt(pindala)


kokku = 0
for x in range(3):
    täringud = random.randint(1, 6)
    kokku = kokku + täringud
    print(kokku)
