abcd = []
ef = []
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

abcd = [a,b,c,d]
ef = [e,f]

abcd.sort()
ans = max(ef) + abcd[1] + abcd[2] + abcd[3]

print(ans)
