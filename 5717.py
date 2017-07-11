stat = True
while(stat==True):
    x = input().split()
    a = int(x[0])
    b = int(x[1])
    if a==0 and b==0:
        stat = False
        break
    else:
        print(a+b)