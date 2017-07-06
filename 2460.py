total = 0
maxi = 0
for i in range(0,10):
    a = input().split()
    total -= int(a[0])
    total += int(a[1])
    if maxi < total:
        maxi = total

print (maxi)
