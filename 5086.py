
con = True
while(con == True):
    n = input().split()
    a = int(n[0])
    b = int(n[1])
    if a==0 and b==0:
        con=False
        break
    elif a//b>0 and a%b==0:
        print("multiple")
    elif b//a>0 and b%a==0:
        print("factor")
    else:
        print("neither")