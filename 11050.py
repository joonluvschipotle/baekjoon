import math
a = input().split()
n = int(a[0])
k = int(a[1])
ans = 1

for i in range((n-k)+1,n+1):
    ans = ans*i


ans = ans//math.factorial(k)

print (ans)
