n = int(input())
nums = input().split()
v = int(input())


freq = [0]*202
for i in nums:
    freq[int(i)]+=1

print(freq[v])