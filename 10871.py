a = input().split()
dfdf = input().split()
n = int(a[0])
x = int(a[1])
list1 = []

for i in range(0,n):
    list1.append(int(dfdf[i]))

for i in list1:
    if i < x:
        print(i,end=" ")