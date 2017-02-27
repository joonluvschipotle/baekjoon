a = input().split()
n = int(a[0])
p = int(a[1])
remnant = []
remnant.append(n)
cycle = []

for i in range(1,1000):
    remnant.append((remnant[i-1]*n)%p)

flag = 0

for i in range(30,len(remnant)):
    if remnant[29] == remnant[i]:
        flag = 1
        for j in range(29,len(remnant)):
            if remnant[j] == remnant[i]:
                cycle.append(remnant[j]
                if flag!=0 and remnant[j]


print (remnant)
