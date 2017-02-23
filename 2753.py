a = input()
b = int(a)
if b%4 == 0:
    if b%400 == 0:
        print (1)
    elif b%100 == 0:
        print (0)
    else:
        print (1)
else:
    print (0)
