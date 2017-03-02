nums = []
sums = 0
for i in range(0,7):
    x = int(input())
    if x%2 != 0:
        sums += x
        nums.append(x)

if len(nums) == 0:
    print (-1)
else:
    print (sums)
    print (min(nums))
