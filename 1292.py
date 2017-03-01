c = input().split()
a = int(c[0])
b = int(c[1])
num = []
ans = 0
if b > 10:
    c = int(b/3)
else:
    c = b

for i in range(0,c+1):
    j = i
    while (j!=0):
        num.append(i)
        j -=1

for i in range(a,b+1):
    ans+=num[i-1]

print (ans)
