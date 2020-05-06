def sorteerimine(lis):
    kokku = 0
    for x in lis:
        if x%2 == 0:
            kokku = kokku + 1
    return kokku

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arv = sorteerimine(lis)
print (arv)