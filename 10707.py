a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

x = a*p
y = b
if p > c:
    y +=(p-c)*d

if x<y:
    print(x)
else:
    print(y)