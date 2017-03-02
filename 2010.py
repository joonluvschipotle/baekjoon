n = int(input())
inputs = []
ans = 0
for i in range(0,n):
    inputs.append(int(input()))
    ans += inputs[i]-1

print (ans+1)
