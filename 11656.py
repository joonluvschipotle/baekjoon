a = input()
ans = []
for i in range(0,len(a)):
    ans.append(a[i:])

ans.sort()
for i in ans:
    print (i)
