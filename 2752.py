a = input().split()
b = []
for i in range(0,3):
    b.append(int(a[i]))

b.sort()

for i in b:
    print (i,end=" ")
