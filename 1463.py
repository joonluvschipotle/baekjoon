number = int(input())
d = [0]*1000001

def makeOne(n):
    if n == 1:
        return 0
    if d[n] > 0:
        return d[n]
    d[n] = makeOne(n-1) + 1
    if n%2 == 0:
        temp = makeOne(n//2) + 1
        if d[n] > temp:
            d[n] = temp
    if n%3 == 0:
        temp = makeOne(n//3) + 1
        if d[n] > temp:
            d[n] = temp
    return d[n]

print (makeOne(number))