a = input().split()
h = int(a[0])
m = int(a[1])

if m > 44:
    print (h,m-45)
else:
    if h == 0:
        h = 23
        m = m+15
        print (h,m)
    else:
        h-=1
        m = m+15
        print (h,m)

