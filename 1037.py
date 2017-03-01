nums = int(input())
divisor = []
dummy = input().split()
for i in dummy:
    divisor.append(int(i))

if len(divisor) == 2:
    n = divisor[0]*divisor[1]
elif len(divisor) == 1:
    n = divisor[0]*divisor[0]
else:
    n = divisor[0]*divisor[-1]

print (n)
