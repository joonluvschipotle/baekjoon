a = input()
b = a.split()
totalCrack = 0

def crack(n):
    global totalCrack
    if n == [1,1]:
        return 0
    elif n == [1,2]:
        totalCrack +=1
        return 1
    else:
        a = max(n)
        b = min(n)
        totalCrack +=1
        return crack([int(a/2),b]) + crack([int((a/2)+(a%2)),b])


crack([int(b[0]),int(b[1])])
print (totalCrack)
