nums = []
remnants = []
for i in range(0,10):
    remnants.append(int(input())%42)

for i in range(0,10):
    if nums.count(remnants[i]) == 0:
        nums.append(remnants[i])
print (len(nums))
