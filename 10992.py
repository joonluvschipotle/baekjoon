a = int(input())

if a > 1:
    for i in range(1,a):
        for j in range(0,a-i):
            print(" ", end="")
        print("*",end="")
        print(" ",end="")
        for k in range(2,i):
            print("  ", end="")
        if i != 1:
            print("*",end="")
        print("")

for i in range(0,(a*2)-1):
    print("*",end="")
