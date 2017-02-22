def getPrime(number):
    global total
    primeList = [2]
    num = 3

    while (num <= number):
        for x in primeList:
            if (num%x == 0):
                break
            elif(x==primeList[-1]):
                primeList.append(num)
                break
        num += 1
    if(number in primeList):
        total+=1

a = input()
b = input()
c = b.split()
total=0
for num in c:
    getPrime(int(num))



print (total)
