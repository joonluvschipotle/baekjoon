a = input()
b = []
d = []
for num in range(0,int(a)):
    c = input()
    b.append(c.split()[0])
    d.append(c.split()[1])

for num in range(0,int(max(b))-1):
    print (b[num] + " " + d[num])
