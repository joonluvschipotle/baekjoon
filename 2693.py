t = int(input())

for i in range(0,t):
    a = input().split()
    nums = []
    for i in a:
        nums.append(int(i))

    nums.sort()
    ans = nums[-3]
    print (ans)