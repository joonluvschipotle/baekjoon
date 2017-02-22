primeList = [2]

def getPrime(number):
    global primeList
    num = 3

    while (num <= number):
        for x in primeList:
            if (num%x == 0):
                break
            elif(x==primeList[-1]):
                primeList.append(num)
                break
        num += 1

a = input()
b = a.split()
getPrime(int(b[1]))

for num in primeList:
    if (num>=int(b[0])):
        print (num)
