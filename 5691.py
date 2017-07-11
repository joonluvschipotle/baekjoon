trueIt = True
while(trueIt == True):
    df = input().split()
    a = int(df[0])
    b = int(df[1])

    if a == 0 and b == 0:
        trueIt = False
        break
    elif a >= b:
        ans = b-(a-b)
        print(ans)
    else:
        ans = a-(b-a)
        print(ans)