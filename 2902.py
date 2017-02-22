a = input()
b = a[0]
count = 0
for i in range(0,len(a)):
    if a[i]=="-":
        b +=a[i+1]

print (b)
