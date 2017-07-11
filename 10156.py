a = input().split()
k = int(a[0])
n = int(a[1])
m = int(a[2])

ans = k*n-m

if ans > 0:
    print (ans)
else:
    print (0)