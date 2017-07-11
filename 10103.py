ch = 100
sd = 100

n = int(input())
nums = []
for i in range(0,n):
    nums.append(input().split())

for i in nums:
    if int(i[0]) > int(i[1]):
        sd -= int(i[0])
    elif int(i[0]) < int(i[1]):
        ch -= int(i[1])

print (ch)
print (sd)