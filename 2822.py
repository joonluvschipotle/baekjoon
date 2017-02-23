a = []
b = []
for i in range(0,8):
    c = input()
    a.append(c)
    b.append(c)
c = 0
d = []
for i in range(0,5):
    c += int(max(b))
    d.append(a.index(max(b)) + 1)
    b.remove(max(b))

d.sort()
print (c)
for i in range(0,5):
    print(d[i],end="")
    if i!=4:
        print (" ",end="")
