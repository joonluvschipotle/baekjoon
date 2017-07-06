a = input().split()
n = a[0]
b = int(a[1])

ans = 0
for i in range(0,len(n)):
    if ord(n[i]) > 64 and ord(n[i]) < 91:
        dum = ord(n[i])-55
    else:
        dum = int(n[i])
    ans += dum*(b**(len(n)-i-1))
print(ans)
