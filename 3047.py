x = input().split()
nums = []
for i in x:
    nums.append(int(i))
nums.sort()

seq = input()
for i in range(0,len(seq)):
    print (nums[ord(seq[i])-65],end=" ")
