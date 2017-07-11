import math
n = input()
nums = [0] * 10

for i in range(0,len(n)):
    if int(n[i]) == 9:
        nums[6] += 1
    else:
        nums[int(n[i])] += 1

nums[6] = math.ceil(nums[6]/2)

print (max(nums))