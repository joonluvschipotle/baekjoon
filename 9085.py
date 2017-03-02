trials = int(input())
for i in range(0,trials):
    ans = 0
    cases = int(input())
    ints = input().split()
    for j in ints:
        ans += int(j)
    print (ans)
