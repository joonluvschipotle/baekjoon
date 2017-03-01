# S = A[0]*B[0] + ... + A[N-1]*B[N-1]
n = int(input())
a = []
b = []
ans = 0
dummy = input().split()
for i in dummy:
    a.append(int(i))

dummy = input().split()
for i in dummy:
    b.append(int(i))

a.sort()
b.sort()
a.reverse()

for i in range(0,n):
    ans += (a[i]*b[i])

print (ans)
