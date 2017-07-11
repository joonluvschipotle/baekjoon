a = input().split()
b = input().split()
s = 0
t = 0
for i in a:
    s += int(i)

for i in b:
    t += int(i)

if s>=t:
    print(s)
else:
    print(t)