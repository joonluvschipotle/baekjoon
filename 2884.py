a = input().split()
h = int(a[0])
m = int(a[1])

if m == 45:
    print (str(h) + " 00")
elif m > 45 and m <55:
    print (str(h) + " 0" + str(m-45))
elif m > 54:
    print (str(h) + " " + str(m-45))
elif m < 45:
    m += 15
    if h == 0:
        h = 23
    else: h -= 1
    print (str(h) + " " + str(m))
