a = input()

ans = 0
dummy = 0

for i in range(0,len(a)):
    if ord(a[i]) > 64 and ord(a[i]) < 90:
        dummy = ord(a[i])-55
    else:
        dummy = int(a[i])
    ans += dummy * (16**(len(a)-i-1))

print(ans)
