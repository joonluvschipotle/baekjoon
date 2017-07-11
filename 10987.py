a = input()
total = 0
for i in range(0,len(a)):
    if a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u":
        total+=1
print (total)