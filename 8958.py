c = int(input())

for j in range(0,c):
    ans = input()
    total = 0
    count = 1
    for i in range(0,len(ans)):
        if ans[i] == "O":
            total += count
            count += 1
        else:
            count = 1
    print (total)