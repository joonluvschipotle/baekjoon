a = input().upper()
nums = [0]*26

for i in range(0,len(a)):
    nums[ord(a[i])-65] +=1

ans = chr(nums.index(max(nums))+65)
if nums.count(max(nums)) > 1:
    print ("?")
else:
    print (ans)
