def binToOct(x):
    strx = str(x)
    octa = 0
    if len(strx) == 3:
        octa = int(strx[0])*4 + int(strx[1])*2 + int(strx[1])
    elif len(strx) == 2:
        octa = int(strx[0])*2 + int(strx[1])
    else:
        octa = x
    return octa

a = input()
ans = ""
if len(a)%3 == 0:
    for i in range(0,int(len(a)/3)):
        ans += str(binToOct(int(a[3*i:3*(i+1)])))
elif len(a)%3 == 2:
    ans += str(binToOct(int(a[0:2])))
    for i in range(1,int(len(a)/3)):
        ans += str(binToOct(int(a[3*i:3*(i+1)])))
elif len(a)%3 == 1:
    ans += str(binToOct(int(a[0:1])))
    for i in range(1,int(len(a)/3)):
        ans += str(binToOct(int(a[3*i:3*(i+1)])))

print (ans)
