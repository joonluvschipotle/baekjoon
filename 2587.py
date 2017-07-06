nums = []
for i in range(0,5):
    nums.append(int(input()))

nums.sort()

avg = 0
for i in nums:
    avg += i
avg = avg/5

print (int(avg))
print (nums[2])
