def recfac(n):
    if n < 2:
        return 1
    else:
        return n * recfac(n-1)
def iterfuc(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*1
    return fact

print(recfac(5))
print(iterfuc(5))