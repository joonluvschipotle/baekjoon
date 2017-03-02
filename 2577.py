a = int(input())
b = int(input())
c = int(input())
d = str(a*b*c)
nums = [0]*10
for i in range(0,len(d)):
    nums[ord(d[i])-48] +=1

for i in nums:
    print (i)
