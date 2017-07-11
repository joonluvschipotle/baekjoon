a = input()
commas = 1
for i in range(0,len(a)):
    if a[i] == ",":
        commas+=1

print (commas)