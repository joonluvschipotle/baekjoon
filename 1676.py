a = int(input())

d = a//5
if a//25 >= 1:
    d += a//25

if a//125 >= 1:
    d += a//125


print(d)
