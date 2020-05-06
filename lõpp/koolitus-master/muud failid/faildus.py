f = open("Proov.txt", "r")
print(f.read())

f.close()

f = open("Proov.txt", "r")
print(f.readline())

f.close()

f = open("Proov.txt", "r")
for x in f:
    print(x)
    
f.close()

