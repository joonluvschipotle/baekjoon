t = int(input())

for k in range(0,t):
    a = input().split()
    total = 0
    min = 101
    for i in a:
        if int(i)%2==0:
            total+=int(i)
            if min > int(i):
                min = int(i)
    print(total,min)