c = int(input())
for j in range(0,c):
    dfdf = input().split()
    n = int(dfdf[0])
    del dfdf[0]
    total = 0
    for i in dfdf:
        total += int(i)
    avg = total/n
    count = 0
    for i in dfdf:
        if int(i) > avg:
            count += 1

    print("{0:.3f}%".format((count/n)*100))