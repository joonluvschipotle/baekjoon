a = input().split()
b = input().split()
c = input().split()

x = 0
y = 0

if a[0] == b[0]:
    y = int(c[0])
elif a[0] == c[0]:
    y = int(b[0])
else:
    y = int(a[0])


if a[1] == b[1]:
    x = int(c[1])
elif a[1] == c[1]:
    x = int(b[1])
else:
    x = int(a[1])

print(y,x)