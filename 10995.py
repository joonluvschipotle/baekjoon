a = int(input())

for j in range(1,a+1):
    for i in range(1,a+1):
        if j%2!=0:
            print("*",end=" ")
        else:
            print(" *",end="")
    print()