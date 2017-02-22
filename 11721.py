a = input()
x = 0
for i in range(0,10):
    if len(a) < (i*10):
        break
    print (a[i*10:(i*10)+10])
