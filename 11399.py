a = int(input())
nums = input().split()
list1 = []
for i in nums:
    list1.append(int(i))

list1.sort()
total = 0
dummy = 0

for i in range(0,a):
    dummy += list1[i]
    total+= dummy

print(total)
