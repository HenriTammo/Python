def recFac(n):
    if n < 2:
        return 1
    else:
        return n * recFac(n-1)
def iterFuc(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact

print(recFac(5))
print(iterFuc(5))