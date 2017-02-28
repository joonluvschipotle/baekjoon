size = input().split()
n = int(size[0])
m = int(size[1])
array = []
dummy = []
for i in range(0,n):
    beforeInt = input().split()
    for j in beforeInt:
        dummy.append(int(j))
    array.append(dummy)
    dummy = []


k = int(input())
inputs = []
dummytwo = []
ans = []
for i in range(0,k):
    beforeIn = input().split()
    for j in beforeIn:
        dummytwo.append(int(j)-1)
    inputs.append(dummytwo)
    dummytwo = []


for i in inputs:
    total = 0
    for j in range(i[0],i[2]+1):
        for x in range(i[1],i[3]+1):
            total += array[j][x]
    ans.append(total)

print (ans)
