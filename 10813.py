a = input().split()
n = int(a[0])
m = int(a[1])

df = []

for i in range(1,n+1):
    df.append(i)


for i in range(0,m):
    b = input().split()
    temp = df[int(b[0])-1]
    df[int(b[0])-1] = df[int(b[1])-1]
    df[int(b[1])-1] = temp

for i in df:
    print(i,end=" ")