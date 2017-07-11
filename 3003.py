nums = input().split()
intnums = [1,1,2,2,2,8]

for i in range(0,len(nums)):
    intnums[i] -= int(nums[i])
    print(intnums[i],end=" ")
